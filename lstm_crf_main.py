import argparse
import os
import pickle
from lstm_crf_model import LstmCrfModel
import tensorflow as tf
import numpy
import sys
import random
import re
import codecs


def load_parameters(id_folder):
    """
    加载参数
    """
    with open(os.path.join(id_folder, "parameters.pkl"), "rb") as f:
        [parameters] = pickle.load(f)
    return parameters


def load_word2vec(emb_path, id_to_word, word_dim, old_weights):
    """
    加载词向量
    """
    new_weights = old_weights
    sys.stderr.write('Loading pretrained embeddings from {}...\n'.format(emb_path))
    pre_trained = {}
    emb_invalid = 0
    for i, line in enumerate(codecs.open(emb_path, 'r', 'utf-8')):
        line = line.rstrip().split()
        if len(line) == word_dim + 1:
            pre_trained[line[0]] = numpy.array(
                [float(x) for x in line[1:]]
            ).astype(numpy.float32)
        else:
            emb_invalid += 1
    if emb_invalid > 0:
        sys.stderr.write('WARNING: %i invalid lines\n' % emb_invalid)
    c_found = 0
    c_lower = 0
    c_zeros = 0
    n_words = len(id_to_word)
    # Lookup table initialization
    for i in range(n_words):
        word = id_to_word[i]
        if word in pre_trained:
            new_weights[i] = pre_trained[word]
            c_found += 1
        elif word.lower() in pre_trained:
            new_weights[i] = pre_trained[word.lower()]
            c_lower += 1
        elif re.sub('\d', '0', word.lower()) in pre_trained:
            new_weights[i] = pre_trained[
                re.sub('\d', '0', word.lower())
            ]
            c_zeros += 1

    sys.stderr.write('Loaded %i pretrained embeddings.\n' % len(pre_trained))
    sys.stderr.write('%i / %i (%.4f%%) words have been initialized with '
                     'pretrained embeddings.\n' % (
                         c_found + c_lower + c_zeros, n_words,
                         100. * (c_found + c_lower + c_zeros) / n_words)
                     )
    sys.stderr.write('%i found directly, %i after lowercasing, '
                     '%i after lowercasing + zero.\n' % (
                         c_found, c_lower, c_zeros
                     ))
    return new_weights


def load_data(data_dir):
    """
    加载数据
    """
    with open(data_dir, "r") as ff:
        dataset = []
        labels = []
        feature = []
        others = []
        for line in ff:
            line = line.rstrip("\n")
            if len(line) > 0:
                if line.startswith(" "):
                    line = '[space] ' + line[1:]

                splits = line.split(" ")
                labels.append(splits[1])
                feature.append(splits[0])
                if len(splits) > 3:
                    others.append(splits[3:])
            else:
                data = dict()
                data["label"] = labels
                data["feature"] = feature
                data["others"] = others

                bigram_feature = []
                for idx, character in enumerate(data["feature"]):
                    if character == '[BEG]' or character == '[END]' or idx == len(data["feature"]) - 1:
                        bigram_feature.append(character)
                    else:
                        bigram_feature.append(character + data["feature"][idx + 1])

                data["bigram_feature"] = bigram_feature

                dataset.append(data)
                labels = []
                feature = []
                others = []

    return dataset


def feature_id_builder(feature_list, start_feature_id, feature_to_id={}, id_to_feature=[]):
    feature_id = start_feature_id
    for feature in feature_list:
        if not feature in feature_to_id:
            feature_to_id[feature] = feature_id
            id_to_feature.append(feature)
            feature_id += 1
    return feature_id


def load_map(dataset, id_folder, isTrain):
    """
    加载映射表
    """
    if not isTrain:
        with open(os.path.join(id_folder, "maps.pkl"), "rb") as fr:
            char_to_id, id_to_char, tag_to_id, id_to_tag, id_to_pos, bigram_to_id, id_to_bigram = pickle.load(
                fr)
            return char_to_id, id_to_char, tag_to_id, id_to_tag, id_to_pos, bigram_to_id, id_to_bigram

    char_id = 0
    tag_id = 0
    pos_id = 0
    bigram_id = 0
    char_to_id = {}
    id_to_char = []
    tag_to_id = {}
    id_to_tag = []
    pos_to_id = {}
    id_to_pos = []

    bigram_to_id = {}
    id_to_bigram = []
    for data in dataset:
        char_id = feature_id_builder(data["feature"], char_id, char_to_id, id_to_char)
        tag_id = feature_id_builder(data["label"], tag_id, tag_to_id, id_to_tag)
        bigram_id = feature_id_builder(data["bigram_feature"], bigram_id, bigram_to_id, id_to_bigram)

    char_to_id["[[[UNK]]]"] = char_id
    id_to_char.append("[[[UNK]]]")
    char_id += 1

    pos_to_id["[[[UNK]]]"] = pos_id
    id_to_pos.append("[[[UNK]]]")
    pos_id += 1

    bigram_to_id["[[[UNK]]]"] = bigram_id
    id_to_bigram.append("[[[UNK]]]")
    bigram_id += 1

    if not os.path.exists(id_folder):
        os.mkdir(id_folder)

    with open(os.path.join(id_folder, "maps.pkl"), "wb") as fw:
        pickle.dump([char_to_id, id_to_char, tag_to_id, id_to_tag, bigram_to_id, id_to_bigram], fw)
    return char_to_id, id_to_char, tag_to_id, id_to_tag, id_to_pos, bigram_to_id, id_to_bigram


def prepare_data(raw_dataset, char_to_id, tag_to_id, bigram_to_id, parameters):
    dataset = {}
    dataset["label"] = []
    dataset["feature"] = []
    dataset["end_pos"] = []
    dataset["bigram_feature"] = []

    for data in raw_dataset:
        features = []
        for char in data["feature"]:
            if char in char_to_id:
                features.append(char_to_id[char])
            else:
                features.append(char_to_id["[[[UNK]]]"])
            if len(features) >= parameters["sentence_len"]:
                break
        t = len(features)
        for i in range(t, parameters["sentence_len"]):
            features.append(len(char_to_id) - 1)
        dataset["feature"].append(features)

        bigram_features = []
        for char in data["bigram_feature"]:
            if char in bigram_to_id:
                bigram_features.append(bigram_to_id[char])
            else:
                bigram_features.append(bigram_to_id["[[[UNK]]]"])
            if len(bigram_features) >= parameters["sentence_len"]:
                break
        t = len(bigram_features)
        for i in range(t, parameters["sentence_len"]):
            bigram_features.append(len(bigram_to_id) - 1)
        dataset["bigram_feature"].append(bigram_features)

        labels = []
        for tag in data["label"]:
            if tag in tag_to_id:
                labels.append(tag_to_id[tag])
            else:
                labels.append(0)
            if len(labels) >= parameters["sentence_len"]:
                break
        t = len(labels)
        for i in range(t, parameters["sentence_len"]):
            labels.append(0)
        dataset["label"].append(labels)

        dataset["end_pos"].append(t)

    return dataset


def eval(test_dataset, test_raw_dataset, id_to_tag, parameters):
    batch_size = 1
    total_batch = int(len(test_dataset["label"]) / batch_size)
    sum_good = [0 for x in range(parameters["label_sum"])]
    sum_pred = [0 for x in range(parameters["label_sum"])]
    sum_oracle = [0 for x in range(parameters["label_sum"])]
    # Loop over all batches
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('%s.meta' % (parameters["mod_trained"]))
        new_saver.restore(sess, '%s' % (parameters["mod_trained"]))

        graph = tf.get_default_graph()

        model_x = graph.get_tensor_by_name('x:0')
        model_y = graph.get_tensor_by_name('y:0')
        model_end_pos = graph.get_tensor_by_name('Placeholder:0')
        model_dropout = graph.get_tensor_by_name('Dropout:0')
        model_logits = graph.get_tensor_by_name('logits:0')
        model_trans = graph.get_tensor_by_name('transitions:0')

        for i in range(total_batch):
            batch_xs, batch_ys = test_dataset["feature"][(i * batch_size):((i + 1) * batch_size)], \
                                 test_dataset["label"][(i * batch_size):((i + 1) * batch_size)]
            batch_end = test_dataset["end_pos"][(i * batch_size):((i + 1) * batch_size)]

            # Run optimization op (backprop) and cost op (to get loss value)
            logits, trans = sess.run([model_logits, model_trans], feed_dict={model_x: batch_xs,
                                                                             model_y: batch_ys,
                                                                             model_end_pos: batch_end,
                                                                             model_dropout: 1.0})
            paths = []
            for index, logit in enumerate(logits):
                logit = logit[:batch_end[index]]
                path, _ = tf.contrib.crf.viterbi_decode(logit, trans)
                paths.append(path)

            oracle = batch_ys
            for batch in range(len(paths)):
                pred_list = []
                char_list = []
                for k in range(batch_end[batch]):
                    pred_list.append(id_to_tag[paths[batch][k]])
                    char_list.append(test_raw_dataset[i]["feature"][k])

                print("%s\t%s" % (" ".join(pred_list), " ".join(char_list)))


def test(test_dataset, parameters, model, sess):
    # batch_size = parameters["batch_size"]
    batch_size = 1
    total_batch = int(len(test_dataset["label"]) / batch_size)
    sum_good = [0 for x in range(parameters["label_sum"])]
    sum_pred = [0 for x in range(parameters["label_sum"])]
    sum_oracle = [0 for x in range(parameters["label_sum"])]
    # Loop over all batches
    for i in range(total_batch):
        batch_xs, batch_ys = test_dataset["feature"][(i * batch_size):((i + 1) * batch_size)], \
                             test_dataset["label"][(i * batch_size):((i + 1) * batch_size)]

        batch_bigram_feature = test_dataset["bigram_feature"][(i * batch_size):((i + 1) * batch_size)]
        batch_end = test_dataset["end_pos"][(i * batch_size):((i + 1) * batch_size)]

        # Run optimization op (backprop) and cost op (to get loss value)
        logits, trans = sess.run([model.logits, model.trans], feed_dict={model.x: batch_xs,
                                                                         model.y: batch_ys,
                                                                         model.bigram: batch_bigram_feature,
                                                                         # model.part_of_speech: batch_part_of_speech,
                                                                         model.end_pos: batch_end,
                                                                         model.dropout: 1.0})

        preds = model.decode(logits, batch_end, trans)

        oracle = batch_ys

        for batch in range(len(preds)):
            for i in range(batch_end[batch]):
                pred_label = preds[batch][i]
                oracle_label = oracle[batch][i]
                sum_pred[pred_label] += 1
                sum_oracle[oracle_label] += 1
                if pred_label == oracle_label:
                    sum_good[pred_label] += 1

    for i in range(parameters["label_sum"]):
        print("label_%i precision[%.2f] recall[%.2f] oracle_sum[%i]" % (
        i, sum_good[i] * 100.0 / sum_pred[i] if sum_pred[i] > 0 else 0.0,
        sum_good[i] * 100.0 / sum_oracle[i] if sum_oracle[i] > 0 else 0.0,
        sum_oracle[i]))

    print("label_all precision[%.2f] recall[%.2f] oracle_sum[%i]" % (
    sum(sum_good) * 100.0 / sum(sum_pred) if sum(sum_pred) > 0 else 0.0,
    sum(sum_good) * 100.0 / sum(sum_oracle) if sum(sum_oracle) > 0 else 0.0,
    sum(sum_oracle)))
    sys.stdout.flush()

    return (sum(sum_good) * 100.0 / sum(sum_pred) if sum(sum_pred) > 0 else 0.0)


def train(train_dataset, test_dataset, parameters):
    tf.set_random_seed(1234)
    random.seed(50)
    numpy.random.seed(123)
    training_epochs = 1000
    learning_rate = 0.01
    batch_size = parameters["batch_size"]
    display_step = 1

    model = LstmCrfModel(parameters)
    global_step = tf.Variable(0, name='global_step', trainable=False)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate)

    grads_vars = optimizer.compute_gradients(model.loss)
    capped_grads_vars = [[tf.clip_by_value(g, -5.0, 5.0), v]
                         for g, v in grads_vars]
    train_op = optimizer.apply_gradients(capped_grads_vars, global_step)
    init = tf.global_variables_initializer()

    pre_prec = 0.0
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        saver = tf.train.Saver(max_to_keep=5)
        sess.run(init)
        if parameters["wordvec_file"] != "":
            emb_weights = sess.run(model.embedding.read_value())
            emb_weights = load_word2vec(parameters["wordvec_file"], id_to_char, parameters["embedding_dim"],
                                        emb_weights)
            sess.run(model.embedding.assign(emb_weights))
        if parameters["bigram_wordvec_file"] != "":
            emb_weights2 = sess.run(model.bigram_embedding.read_value())
            emb_weights2 = load_word2vec(parameters["bigram_wordvec_file"], id_to_bigram,
                                         parameters["embedding_dim"] / 4, emb_weights2)
            sess.run(model.bigram_embedding.assign(emb_weights2))
        for epoch in range(training_epochs):
            avg_cost = 0.0
            total_batch = int(len(train_dataset["label"]) / batch_size) + 1
            # Loop over all batches
            ids = range(len(train_dataset["label"]))
            permutation = numpy.random.permutation(ids)

            # print permutation
            for i in range(total_batch):
                batch_xs = []
                batch_ys = []
                batch_bigram_feature = []
                batch_end = []
                for x in range(i * batch_size, (i + 1) * batch_size):
                    if x < len(permutation):
                        batch_xs.append(train_dataset["feature"][permutation[x]])
                        batch_ys.append(train_dataset["label"][permutation[x]])
                        batch_bigram_feature.append(train_dataset["bigram_feature"][permutation[x]])
                        batch_end.append(train_dataset["end_pos"][permutation[x]])

                if len(batch_xs) == 0:
                    continue
                _, c = sess.run([train_op, model.loss], feed_dict={model.x: batch_xs,
                                                                   model.y: batch_ys,
                                                                   model.bigram: batch_bigram_feature,
                                                                   model.end_pos: batch_end,
                                                                   model.dropout: parameters["dropout"]})
                # 计算平均loss
                avg_cost += c / total_batch

            # Display logs per epoch step
            if (epoch + 1) % display_step == 0:
                print("Epoch: %d cost=%.5f" % (epoch + 1, avg_cost))
                print("test result:")
                prec = test(test_dataset, parameters, model, sess)
                if prec > pre_prec:
                    pre_prec = prec
                    print("new prec is [%.2f]" % (pre_prec))
                    if not os.path.exists(parameters["save_path"]):
                        os.mkdir(parameters["save_path"])
                    saver.save(sess, os.path.join(parameters["save_path"], "mod"), int(pre_prec * 100))


if __name__ == "__main__":
    # ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_file", type=str, default="data/train.txt")
    parser.add_argument("--dev_file", type=str, default="data/dev.txt")
    parser.add_argument("--test_file", type=str, default="data/test.txt")
    # parser.add_argument("--wordvec_file", type=str, default="data/jinrong_vec")
    # parser.add_argument("--bigram_wordvec_file", type=str, default="data/jinrong_bigram_vec")
    parser.add_argument("--wordvec_file", type=str, default="")
    parser.add_argument("--bigram_wordvec_file", type=str, default="")
    parser.add_argument("--mod_file", type=str, default="model")
    parser.add_argument("--mod_trained", type=str, default="model_trained/mod-9933")
    parser.add_argument("--id_folder", type=str, default="id_folder")
    parser.add_argument("--embedding_dim", type=int, default=400, help="Word2Vec dimension")
    parser.add_argument("--hidden_dim", type=int, default=800, help="Word2Vec dimension")
    parser.add_argument("--sentence_len", type=int, default=400, help="Word2Vec dimension")
    parser.add_argument("--batch_size", type=int, default=10, help="Word2Vec dimension")
    parser.add_argument("--dropout", type=float, default=0.8, help="Word2Vec dimension")
    parser.add_argument("--train", type=bool, default=True, help="active this flag to train the model")
    parser.add_argument("--test", type=bool, default=True, help="active this flag to test the model")
    args = parser.parse_args()

    # PARAMETERS
    parameters = {
        "embedding_dim": args.embedding_dim,
        "sentence_len": args.sentence_len,
        "mod_trained": args.mod_trained,
        "save_path": args.mod_file,
        "hidden_dim": args.hidden_dim,
        "batch_size": args.batch_size,
        "dropout": args.dropout,
        "wordvec_file": args.wordvec_file,
        "bigram_wordvec_file": args.bigram_wordvec_file
    }

    train_raw_dataset = load_data(args.train_file)
    test_raw_dataset = load_data(args.test_file)
    dev_raw_dataset = load_data(args.dev_file)

    char_to_id, id_to_char, tag_to_id, id_to_tag, id_to_pos, bigram_to_id, id_to_bigram = \
        load_map(train_raw_dataset, args.id_folder, args.train)

    train_data = prepare_data(train_raw_dataset, char_to_id, tag_to_id, bigram_to_id, parameters)
    dev_data = prepare_data(dev_raw_dataset, char_to_id, tag_to_id, bigram_to_id, parameters)
    test_data = prepare_data(test_raw_dataset, char_to_id, tag_to_id, bigram_to_id, parameters)

    parameters["feature_sum"] = len(id_to_char)
    parameters["label_sum"] = len(id_to_tag)
    parameters["bigram_feature_sum"] = len(id_to_bigram)

    with open(os.path.join(args.id_folder, "parameters.pkl"), "wb") as f:
        pickle.dump([parameters], f)

    if args.train:
        train(train_data, dev_data, parameters)
    if args.test:
        eval(test_data, test_raw_dataset, id_to_tag, parameters)
