# -*- coding: utf-8 -*-


import os
import pickle
import numpy as np


def allowed_transitions(id2target, encoding_type='bio', include_start_end=False):
    """
    别名：:class:`fastNLP.modules.allowed_transitions`  :class:`fastNLP.modules.decoder.allowed_transitions`

    给定一个id到label的映射表，返回所有可以跳转的(from_tag_id, to_tag_id)列表。

    :param dict id2target: key是label的indices，value是str类型的tag或tag-label。value可以是只有tag的, 比如"B", "M"; 也可以是
        "B-NN", "M-NN", tag和label之间一定要用"-"隔开。一般可以通过Vocabulary.idx2word得到id2label。
    :param str encoding_type: 支持"bio", "bmes", "bmeso", "bioes"。
    :param bool include_start_end: 是否包含开始与结尾的转换。比如在bio中，b/o可以在开头，但是i不能在开头；
        为True，返回的结果中会包含(start_idx, b_idx), (start_idx, o_idx), 但是不包含(start_idx, i_idx);
        start_idx=len(id2label), end_idx=len(id2label)+1。为False, 返回的结果中不含与开始结尾相关的内容
    :return: List[Tuple(int, int)]], 内部的Tuple是可以进行跳转的(from_tag_id, to_tag_id)。
    """
    num_tags = len(id2target)
    start_idx = num_tags
    end_idx = num_tags + 1
    encoding_type = encoding_type.lower()
    allowed_trans = []
    id_label_lst = list(id2target.items())
    if include_start_end:
        id_label_lst += [(start_idx, '[beg]'), (end_idx, '[end]')]

    def split_tag_label(from_label):
        from_label = from_label.lower()
        if from_label in ['[beg]', '[end]']:
            from_tag = from_label
            from_label = ''
        else:
            from_tag = from_label[:1]
            from_label = from_label[2:]
        return from_tag, from_label

    for from_id, from_label in id_label_lst:
        if from_label in ['<pad>', '<unk>']:
            continue
        from_tag, from_label = split_tag_label(from_label)
        for to_id, to_label in id_label_lst:
            if to_label in ['<pad>', '<unk>']:
                continue
            to_tag, to_label = split_tag_label(to_label)
            if _is_transition_allowed(encoding_type, from_tag, from_label, to_tag, to_label):
                allowed_trans.append((from_id, to_id))
    return allowed_trans


def _is_transition_allowed(encoding_type, from_tag, from_label, to_tag, to_label):
    """

    :param str encoding_type: 支持"BIO", "BMES", "BEMSO", 'bioes'。
    :param str from_tag: 比如"B", "M"之类的标注tag. 还包括start, end等两种特殊tag
    :param str from_label: 比如"PER", "LOC"等label
    :param str to_tag: 比如"B", "M"之类的标注tag. 还包括start, end等两种特殊tag
    :param str to_label: 比如"PER", "LOC"等label
    :return: bool，能否跃迁
    """
    if to_tag == '[beg]' or from_tag == '[end]':
        return False
    encoding_type = encoding_type.lower()
    if encoding_type == 'bio':
        """
        第一行是to_tag, 第一列是from_tag. y任意条件下可转，-只有在label相同时可转，n不可转
        +-------+---+---+---+-------+-----+
        |       | B | I | O | start | end |
        +-------+---+---+---+-------+-----+
        |   B   | y | - | y | n     | y   |
        +-------+---+---+---+-------+-----+
        |   I   | y | - | y | n     | y   |
        +-------+---+---+---+-------+-----+
        |   O   | y | n | y | n     | y   |
        +-------+---+---+---+-------+-----+
        | start | y | n | y | n     | n   |
        +-------+---+---+---+-------+-----+
        | end   | n | n | n | n     | n   |
        +-------+---+---+---+-------+-----+
        """
        if from_tag == '[beg]':
            return to_tag in ('b', 'o')
        elif from_tag in ['b', 'i']:
            return any([to_tag in ['[end]', 'b', 'o'], to_tag == 'i' and from_label == to_label])
        elif from_tag == 'o':
            return to_tag in ['[end]', 'b', 'o']
        else:
            raise ValueError("Unexpect tag {}. Expect only 'B', 'I', 'O'.".format(from_tag))
    else:
        raise ValueError("Only support BIO, BMES, BMESO, BIOES encoding type, got {}.".format(encoding_type))


def add_constrain_to_trans(trans, is_stack=False):
    id2target = {}
    with open(os.path.join("id_folder_ner", "maps.pkl"), "rb") as f:
        char_to_id, id_to_char, tag_to_id, id_to_tag, pos_to_id, id_to_pos, \
        bigram_to_id, id_to_bigram, tag_stack_to_id, id_to_tag_stack = pickle.load(f, encoding='utf-8')
        if is_stack:
            for idx in range(len(id_to_tag_stack)):
                id2target[idx] = id_to_tag_stack[idx]
        else:
            for idx in range(len(id_to_tag)):
                id2target[idx] = id_to_tag[idx]

    allowed_transitions_list = allowed_transitions(id2target)

    trans = np.array(trans)
    matrix_size = len(trans)

    constrain = np.array([[-10000] * matrix_size for _ in range(matrix_size)])

    for from_tag_id, to_tag_id in allowed_transitions_list:
        constrain[from_tag_id][to_tag_id] = 0

    trans += constrain

    return trans.tolist()


if __name__ == '__main__':
    constrain = [[0] * 37 for _ in range(37)]
    trans_constrain = add_constrain_to_trans(constrain)
    print(trans_constrain)
