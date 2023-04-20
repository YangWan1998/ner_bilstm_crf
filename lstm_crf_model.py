import tensorflow as tf
import numpy as np
from tensorflow.contrib.layers.python.layers import initializers


class LstmCrfModel:
    def __init__(self, parameters):
        self.x = tf.placeholder(tf.int32, [None, parameters["sentence_len"]], "x")
        self.bigram = tf.placeholder(tf.int32, [None, parameters["sentence_len"]], "bigram")

        self.y = tf.placeholder(tf.int32, [None, parameters["sentence_len"]], "y")
        self.end_pos = tf.placeholder(dtype=tf.int32, shape=[None])
        self.embedding = tf.get_variable("embedding", [parameters["feature_sum"], parameters["embedding_dim"]],
                                         dtype=tf.float32)
        embed_lookup1 = tf.nn.embedding_lookup(self.embedding, self.x)

        self.bigram_embedding = tf.get_variable("bigram_embedding",
                                                [parameters["bigram_feature_sum"], parameters["embedding_dim"] / 4],
                                                dtype=tf.float32)
        embed_lookup3 = tf.nn.embedding_lookup(self.bigram_embedding, self.bigram)

        concate_embedings = [embed_lookup1, embed_lookup3]

        embed_lookup = tf.concat(concate_embedings, axis=-1, name="concat")

        self.dropout = tf.placeholder(dtype=tf.float32,
                                      name="Dropout")
        lstm_input = tf.nn.dropout(embed_lookup, self.dropout)
        lstm_output = self.biLSTM_layer(lstm_input, parameters)
        hidden = tf.reshape(lstm_output, shape=[-1, parameters["hidden_dim"] * 2])

        self.w = tf.get_variable("softmax_w", [parameters["hidden_dim"] * 2, parameters["label_sum"]], dtype=tf.float32)
        self.b = tf.get_variable("softmax_b", [parameters["label_sum"]], dtype=tf.float32)
        final_output = tf.matmul(hidden, self.w) + self.b
        self.logits = tf.reshape(final_output, [-1, parameters["sentence_len"], parameters["label_sum"]], "logits")

        self.trans = tf.get_variable(
            "transitions",
            shape=[parameters["label_sum"], parameters["label_sum"]])

        self.cost, self.trans = tf.contrib.crf.crf_log_likelihood(
            inputs=self.logits,
            tag_indices=self.y,
            sequence_lengths=self.end_pos,
            transition_params=self.trans)

        self.loss = tf.reduce_mean(-self.cost)

    def biLSTM_layer(self, lstm_inputs, parameters):
        """
        :param lstm_inputs: [batch_size, num_steps, emb_size] 
        :return: [batch_size, num_steps, 2*lstm_dim] 
        """
        with tf.variable_scope("char_BiLSTM"):
            lstm_cell = {}
            for direction in ["forward", "backward"]:
                with tf.variable_scope(direction):
                    lstm_cell[direction] = tf.contrib.rnn.BasicLSTMCell(parameters["hidden_dim"])
            outputs, final_states = tf.nn.bidirectional_dynamic_rnn(
                lstm_cell["forward"],
                lstm_cell["backward"],
                lstm_inputs,
                sequence_length=self.end_pos,
                dtype=tf.float32)
        return tf.concat(outputs, axis=2)

    def decode(self, logits, lengths, matrix):
        """
        :param logits: [batch_size, num_steps, num_tags]float32, logits
        :param lengths: [batch_size]int32, real length of each sequence
        :param matrix: transaction matrix for inference
        :return:
        """
        paths = []
        for index, logit in enumerate(logits):
            if lengths[index]:
                logit = logit[:lengths[index]]
                path, _ = tf.contrib.crf.viterbi_decode(logit, matrix)
            else:
                path = []
            paths.append(path)
        return paths


if __name__ == '__main__':
    pass
