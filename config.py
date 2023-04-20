reflect = {
    "美元": ["USD","$"],
    "日元": ["JPY"],
    "欧元": ["EUR"],
    "英镑": ["GBP"],
    "港元": ["HKD"],
    '澳元':['AUD'],
    "人民币":['￥','CNY','RMB','￥']
}

key_all = {
    "GnrCorpName": 0,
    # "CntntDsc":0,
    'diyawu': 0,
    'diyajine': 0,
    "MrtgCltlPrvPpL": 0,
    "GntDsc": 0,
    "baozhengjine": 0
}

bidui_dict = {
    'RepymtSrc': '0',  # 金额描述
    'CrClntName': '1',  # 授信客户名称
    'BussKind1': '2',  # 业务品种1
    'Ccy4': '3',  # 币种
    'SingleAmt': '4',  # 单笔金额
    'InfoDsc': '6',  # 到期日描述
    'InfoDsc2': '5',  # 期限描述
    'RateScop': '7',  # 利率
    'FdcrPyNm1': '8',  # 受托支付
    'Usage8': '9',  # 用途
    'CmdtyDsc1': '10',  # 保证金描述
    'GnrInfoList': '11',  # 列表  保证人  保证人描述
    'PledgeInfoList': "12",  # 列表 抵质押物提供人  内容描述
    'PrmCndInfoList': '13',  # list  前提子条件
    'RsrvField1': '14',  # 保留字段1
    'RsrvField2': '15',  # 保留字段1
    'KpArryInfoList': '16',  # DtlInfo 保留信息
    'GnrCorpName': '17',
    'GntDsc': '18',
    'MrtgCltlPrvPpL': '19',
    # 'CntntDsc':'20',
    'diyawu': '20',
    'diyajine': '21',
    'baozhengjine': '22'

}

danbaoren_list = 'GnrInfoList'
diyawu_list = 'PledgeInfoList'
diyashuoming_list = 'CntntDsc'
compare_list=[
 {
        'kehu': 'CrClntName',
        'yewupinzhong': 'BussKind1',
        'biaozhun_yewupinzhong':'StdBussKind1',
        'jine': 'RepymtSrc',
        'SingleAmt': 'SingleAmt',
        'bizhong': 'Ccy4',
        'daoqiri': 'InfoDsc', # 到期日
        'biaozhundaoqiri':'StdInfoDsc',
        'qixian': 'InfoDsc2',
        'biaozhunqixian':'StdInfoDsc2',
        'lilvmiaoshu': 'RateScop',
        'ex_lilvbiaozhun': 'StdRateScop_baserate',
        'ex_lilvleixing': 'StdRateScop_Xibor',
        'ex_lilvqixian': 'StdRateScop_period',
        'ex_lilv': 'StdRateScop_int_rate',
        'ex_fudongbili': 'StdRateScop_floatrate',
        'ex_fudongXBPS': 'StdRateScop_floatBPS',
        'shoutuozhifu': 'FdcrPyNm1',
        'ex_zhifufangshi': 'StdFdcrPyNm1_method',
        'ex_shoutuozhifujine': 'StdFdcrPyNm1_amount',
        'ex_shoutuozhifudiuxiang': 'StdFdcrPyNm1_object',
        'yongtu': 'Usage8',
        'baozhengjinmiaoshu': 'CmdtyDsc1',
        'ex_baozhengjinbili': 'StdCmdtyDsc1_ratio',
        'ex_baozhengjinjine': 'StdCmdtyDsc1_amount',
        'baozhengrendanbaomiaoshu': 'GntDsc',
        'ex_baozhengren': 'GnrCorpName',
        'diyawu': 'CntntDsc',
        'ex_diyawutigongren': 'MrtgCltlPrvPpL',
        'baozhengrendanbaomiaoshu_score': 'GntDsc_score',
        'ex_baozhengren_score': 'GnrCorpName_score',
        'diyawu_score': 'CntntDsc_score',
        'ex_diyawutigongren_score': 'MrtgCltlPrvPpL_score',
        'danbao_list':'GnrInfoLst',#'保证人信息列表GnrInfoLst':'',
        'diya_list':'PledgeInfoLst',#'抵押物信息列表PledgeInfoLst':'',
    },
                   {
        'kehu': '授信客户名称crclntname',
        'yewupinzhong': '业务品种busskind1',
        'biaozhun_yewupinzhong':'标准业务品种StdBussKind1',
        'jine': '币种金额描述RepymtSrc',
        'SingleAmt': '单笔金额singleamt',
        'bizhong': '币种ccy4',
        'daoqiri': '到期日信息描述infodsc', # 到期日
        'biaozhundaoqiri':'标准到期日StdInfoDsc',
        'qixian': '期限信息描述infodsc2',
        'biaozhunqixian':'标准期限StdInfoDsc2',
        'lilvmiaoshu': '利率描述ratescop',
        'ex_lilvbiaozhun': '利率标准StdRateScop_baserate',
        'ex_lilvleixing': '利率Xibor-StdRateScop_Xibor',
        'ex_lilvqixian': '利率期限StdRateScop_period',
        'ex_lilv': '标准利率StdRateScop_int_rate',
        'ex_fudongbili': '利率浮动比例StdRateScop_floatrate',
        'ex_fudongXBPS': '利率浮动XBPS-StdRateScop_floatBPS',
        'shoutuozhifu': '受托支付信息fdcrpynm1',
        'ex_zhifufangshi': '支付方式StdFdcrPyNm1_method',
        'ex_shoutuozhifujine': '支付金额StdFdcrPyNm1_amount',
        'ex_shoutuozhifudiuxiang': '支付对象StdFdcrPyNm1_object',
        'yongtu': '用途usage8',
        'baozhengjinmiaoshu': '保证金描述cmdtydsc1',
        'ex_baozhengjinbili': '保证金比例StdCmdtyDsc1_ratio',
        'ex_baozhengjinjine': '保证金金额StdCmdtyDsc1_amount',
        'baozhengrendanbaomiaoshu': '担保描述GntDsc',
        'ex_baozhengren': '保证人名称GnrCorpName',
        'diyawu': '抵质押物内容描述CntntDsc',
        'ex_diyawutigongren': '抵质押物提供人名称MrtgCltlPrvPpL',
        'baozhengrendanbaomiaoshu_score': '担保描述置信度GntDsc_score',
        'ex_baozhengren_score': '保证人名称置信度GnrCorpName_score',
        'diyawu_score': '抵质押物内容描述置信度CntntDsc_score',
        'ex_diyawutigongren_score': '抵质押物提供人名称置信度MrtgCltlPrvPpL_score',
        'danbao_list':'担保描述列表GnrInfoLst',#'保证人信息列表GnrInfoLst':'',
        'diya_list':'抵押物描述列表PledgeInfoLst',#'抵押物信息列表PledgeInfoLst':'',
    }
    ]
category_b_s={
    'lilvmiaoshu':['ex_lilvbiaozhun','ex_lilvleixing','ex_lilvqixian','ex_lilv','ex_fudongbili','ex_fudongXBPS'],
    'shoutuozhifu':['ex_zhifufangshi','ex_shoutuozhifujine','ex_shoutuozhifudiuxiang'],
     'baozhengjinmiaoshu':['ex_baozhengjinbili','ex_baozhengjinjine'],
    'baozhengrendanbaomiaoshu':['ex_baozhengren'],
    'diyawu':['ex_diyawutigongren'],
    
}
pinyin=['kehu','yewupinzhong','jine','bizhong','daoqiri','qixian','lilvmiaoshu','ex_lilvbiaozhun','ex_lilvleixing','ex_lilvqixian','ex_lilv','ex_fudongbili',
        'ex_fudongXBPS','shoutuozhifu','ex_zhifufangshi','ex_shoutuozhifujine','ex_shoutuozhifudiuxiang','yongtu','baozhengjinmiaoshu','ex_baozhengjinbili',
        'ex_baozhengjinjine','baozhengrendanbaomiaoshu','ex_baozhengren','diyawu','ex_diyawutigongren']
pinyin_list=['kehu','yewupinzhong','jine','bizhong','daoqiri','qixian','lilvmiaoshu','ex_lilvbiaozhun','ex_lilvleixing','ex_lilvqixian','ex_lilv','ex_fudongbili',
        'ex_fudongXBPS','shoutuozhifu','ex_zhifufangshi','ex_shoutuozhifujine','ex_shoutuozhifudiuxiang','yongtu','baozhengjinmiaoshu','ex_baozhengjinbili',
        'ex_baozhengjinjine','danbao_list','diyawu_list']

stand_colums=['File','CrClntName','BussKind1','RepymtSrc','Ccy4','InfoDsc','InfoDsc2','RateScop', 'StdRateScop_baserate',
             'StdRateScop_Xibor', 'StdRateScop_period','StdRateScop_int_rate','StdRateScop_floatrate', 'StdRateScop_floatBPS',
             'FdcrPyNm1','StdFdcrPyNm1_method','StdFdcrPyNm1_amount','StdFdcrPyNm1_object','Usage8','CmdtyDsc1',
             'StdCmdtyDsc1_ratio','StdCmdtyDsc1_amount','GntDsc','GnrCorpName','CntntDsc','MrtgCltlPrvPpL',]

# excel_columns = ['金额描述', '授信客户名称', '业务品种', '币种', '单笔金额',
#                  '到期日', '期限描述', '利率', '受托支付', '用途',
#                  '保证金描述', '保证人列表', '抵质押物列表',
#                  '前提子条件','保留信息']
excel_columns = ['File', 'CrClntName', 'CrClntName_score',
                 'BussKind1', 'BussKind1_score', 'RepymtSrc',
                 'Ccy4', 'Ccy4_score', 'SingleAmt', 'SingleAmt_score', 'InfoDsc', 'InfoDsc_score',
                 'InfoDsc2', 'InfoDsc2_score', 'RateScop', 'RateScop_score',
                 'FdcrPyNm1', 'FdcrPyNm1_score', 'Usage8', 'Usage8_score',
                 'CmdtyDsc1', 'CmdtyDsc1_score', 'GnrInfoLst',
                 'PledgeInfoLst', 'PrmCndInfoList',
                 'KpArryInfoList']
excel_columns1 = ['File', 'CrClntName', 'CrClntName_score',
                  'BussKind1', 'BussKind1_score', 'RepymtSrc', 'RepymtSrc_score',
                  'Ccy4', 'Ccy4_score', 'SingleAmt', 'SingleAmt_score', 'InfoDsc', 'InfoDsc_score',
                  'InfoDsc2', 'InfoDsc2_score', 'RateScop', 'RateScop_score',
                  'FdcrPyNm1', 'FdcrPyNm1_score', 'Usage8', 'Usage8_score',
                  'CmdtyDsc1', 'CmdtyDsc1_score',
                  'GnrInfoLst', 'PledgeInfoLst',
                  'PrmCndInfoList', 'KpArryInfoList']

list_list = ['GnrCorpName', 'MrtgCltlPrvPpL', 'GntDsc', 'CntntDsc']

GN = ['GnrCorpName', 'GntDsc']
GN_1 = ['baozhengrendanbaomiaoshu', 'ex_baozhengren']
P_MC = ['MrtgCltlPrvPpL', 'CntntDsc']

co = ['RepymtSrc', 'CrClntName', 'BussKind1', 'Ccy4', 'SingleAmt',
      'InfoDsc', 'InfoDsc2', 'RateScop', 'FdcrPyNm1', 'Usage8', 'CmdtyDsc1',
      'GnrCorpName', 'GntDsc', 'MrtgCltlPrvPpL', 'CntntDsc']
# 需要检查括号匹配的字段
KHPP = ['CrClntName', 'BussKind1', 'Ccy4',
        'InfoDsc', 'InfoDsc2', 'RateScop', 'FdcrPyNm1', 'Usage8', 'CmdtyDsc1', ]

# CrClntName 客户名称为下面名称时为空
CrClntName_Null = ['该公司', '该客户', '申请人', '公司', '企业']
# 开头结尾处理
dict_chuli = {'kehu_start': ['[BEG]', '“', '客户', '"', '同意',"产管"],
              'kehu_end': ['开立电子银行', '综合授', '综合授信额度','维持','综合'],
              # 'BussKind1'业务品种处理---------此字段不处理
              'yewupinzhong_end': ['￥',"美",'担','金','部','作'],
              'yewupinzhong_start': ['量','房开发','款','立','口保','口','设立','特定权限','业务授信额度',"美",'修改','信额','程贷款'],
              # FdcrPyNm1 受托支付处理
              'shoutuozhifu_start': ['采取', '贷款人', '全部借款人'], 'shoutuozhifu_end': ['方式', '先'],
              # Usage8用途处理
              'yongtu_start': ['用于', '用途为', '用途', ',', '，', '授信用途为', '授信用途为,', '均为', '以', '（', '('], 'yongtu_end': [],
              # CmdtyDsc1保证金描述处理
              'baozhengjin_start': ['收取', '交存', '开票'],
              'baozhengjin_end': [],
              # RateScop 利率描述处理
              'lilvmiaoshu_start': ['押汇', '贷款', '保证金', '金额为', '金额', '金额合计', '合计金额', '民币','款利率'],
              'lilvmiaoshu_end': ['（按相关规定报批，','利率符合','利率按','基准利'],
              # 金额描述处理
              'jine_start': ['金额为', '金额', '金额合计', '合计金额', '民币', '合计','万元','0万元','00万元','000万元','00000'],
              'jine_end': ['（按相关规定报批，', '项'],
              # 到期日处理
              'InfoDsc_start': [],
              'InfoDsc_end': [],
              # 期限处理
              'qixian_start': ['期限', '业务期限为', '贷款期限', '单笔期限', '为', '单笔业务期限', '单笔业务审批期限为', '业务期限',
                                 '均为', '贷款期限', '单笔业务', '付款期限'],
              'qixian_end': ['短期流贷'],
              }

filter_title = ['kehu',]
delete_list_dict= {
'CrClntName':['客户','该公司', '该客户', '申请人', '公司', '企业'],
'CmdtyDsc1':[ '保证金']


}



score_list = ['CrClntName_score', 'BussKind1_score', 'Ccy4_score', 'SingleAmt_score',
              'InfoDsc_score', 'InfoDsc2_score', 'RateScop_score', 'FdcrPyNm1_score',
              'Usage8_score', 'CmdtyDsc1_score',
              ]

CN_NUM = {
    '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
    '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2,
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

CN_UNIT = {
    '十': 10,
    '拾': 10,
    '百': 100,
    '佰': 100,
    '千': 1000,
    '仟': 1000,
    '万': 10000,
    '萬': 10000,
    '亿': 100000000,
    '億': 100000000,
    '兆': 1000000000000,
}
all_list=['CrClntName', 'CrClntName_score', 'BussKind1', 'BussKind1_score', 'RepymtSrc', 'RepymtSrc_score',
          'Ccy4', 'Ccy4_score', 'InfoDsc', 'InfoDsc_score', 'InfoDsc2', 'InfoDsc2_score', 'RateScop', 'RateScop_score',
          'StdRateScop_baserate', 'StdRateScop_baserate_score', 'StdRateScop_Xibor', 'StdRateScop_Xibor_score', 'StdRateScop_period',
          'StdRateScop_period_score', 'StdRateScop_int_rate', 'StdRateScop_int_rate_score', 'StdRateScop_floatrate', 'StdRateScop_floatrate_score',
          'StdRateScop_floatBPS', 'StdRateScop_floatBPS_score', 'FdcrPyNm1', 'FdcrPyNm1_score', 'StdFdcrPyNm1_method', 'StdFdcrPyNm1_method_score',
          'StdFdcrPyNm1_amount', 'StdFdcrPyNm1_amount_score', 'StdFdcrPyNm1_object', 'StdFdcrPyNm1_object_score', 'Usage8', 'Usage8_score',
          'CmdtyDsc1', 'CmdtyDsc1_score', 'StdCmdtyDsc1_ratio', 'StdCmdtyDsc1_ratio_score', 'StdCmdtyDsc1_amount', 'StdCmdtyDsc1_amount_score',
          'GntDsc', 'GntDsc_score', 'GnrCorpName', 'GnrCorpName_score', 'CntntDsc', 'MrtgCltlPrvPpL']
# 接口输出的字段信息
app_data={"ActnLevlCode": "",  "ActnLevlCode_score": "",
             "CrClntName": "","CrClntName_score": "",
             "BussKind1": "", "BussKind1_score": "",  'StdBussKind1':  '',
             "RateScop": "", "RateScop_score": "",
             "Ccy4": "", "Ccy4_score": "",
             "SingleAmt": "", "SingleAmt_score": "",
             "InfoDsc": "", "InfoDsc_score": "", 'StdInfoDsc':'',
          "InfoDsc2": "", "InfoDsc2_score": "", 'StdInfoDsc2':'',
             "CntntDsc": "", "CntntDsc_score": "",
             "RateScop": "", "RateScop_score": "",
             "StdRateScop_baserate": "", "StdRateScop_int_rate": "", "StdRateScop_Xibor": "",
             "StdRateScop_period": "", "StdRateScop_floatrate": "", "StdRateScop_floatBPS": "",
             "FdcrPyNm1": "", "FdcrPyNm1_score": "",
             "StdFdcrPyNm1_method": "", "StdFdcrPyNm1_amount": "", "StdFdcrPyNm1_object": "",
             "Usage8": "", "Usage8_score": "",
             "CmdtyDsc1": "", "CmdtyDsc1_score": "",
             "StdCmdtyDsc1_ratio": "", "StdCmdtyDsc1_amount": "",
             "GnrInfoLst": [
                 {"GnrCorpName": "","GnrCorpName_socre": "","GntDsc":"","GntDsc_score":"" },
                 {"GnrCorpName": "","GnrCorpName_socre": "","GntDsc":"","GntDsc_score":"" }
             ],
             "PledgeInfoLst": [
                 {"CntntDsc": "","CntntDsc_socre": "","MrtgCltlPrvPpL":"","MrtgCltlPrvPpL_score":""},
                 {"CntntDsc": "","CntntDsc_socre": "","MrtgCltlPrvPpL":"","MrtgCltlPrvPpL_score":""},
             ],
          #前提子条件
             "PrmCndInfoLst": [
                 {"PrmCnd": "","PrmCnd_socre": ""},{"PrmCnd": "","PrmCnd_socre": ""}
             ],
          #文字描述
             "RsrvField1" : "" ,"RsrvField1_score" : "" ,
             "RsrvField2" : "" ,"RsrvField2_score" : "" ,
          #明细信息
             "KpArryInfoLst": [{"DtlInfo": "","DtlInfo_socre": ""},
                               {"DtlInfo": "","DtlInfo_socre": ""}] }

zhongwen_dict={
#'序号id':'', #序号id直接加在excel上
'审批意见repymtsrc':'',
'审批意见置信度repymtsrc_score':'',
'授信客户名称crclntname':'',
'授信客户名称置信度crclntname_score':'',
'业务品种busskind1':'',
'业务品种置信度busskind1_score':'',
'币种金额描述CntntDsc':'',
'币种金额描述置信度CntntDsc_score':'',
'币种ccy4':'',
'币种置信度ccy4_score':'',
'单笔金额singleamt':'',
'单笔金额置信度singleamt_score':'',
'到期日信息描述infodsc':'',
'到期日信息描述置信度infodsc_score':'',
'期限信息描述infodsc2':'',
'期限信息描述置信度infodsc2_score':'',
'利率描述ratescop':'',
'利率描述置信度ratescop_score':'',
'受托支付信息fdcrpynm1':'',
'受托支付信息置信度fdcrpynm1_score':'',
'用途usage8':'',
'用途置信度usage8_score':'',
'保证金描述cmdtydsc1':'',
'保证金描述置信度cmdtydsc1_score':'',
'保证人信息列表GnrInfoLst':'',
'抵押物信息列表PledgeInfoLst':'',
'前提条件信息列表PrmCndInfoList':'',
'保留数组信息列表KpArryInfoList':'',
}
list_stad=[
'审批意见File','审批意见置信度File_score',
'授信客户名称crclntname','授信客户名称置信度crclntname_score',
'业务品种busskind1','业务品种置信度busskind1_score',
'币种金额描述RepymtSrc','币种金额描述置信度RepymtSrc_score',
'币种ccy4','币种置信度ccy4_score',
'单笔金额singleamt','单笔金额置信度singleamt_score',
'到期日信息描述infodsc','到期日信息描述置信度infodsc_score',
'期限信息描述infodsc2','期限信息描述置信度infodsc2_score',
'利率描述ratescop','利率描述置信度ratescop_score',
'受托支付信息fdcrpynm1','受托支付信息置信度fdcrpynm1_score',
'用途usage8','用途置信度usage8_score',
'保证金描述cmdtydsc1','保证金描述置信度cmdtydsc1_score',
#'保证人信息列表GnrInfoLst',
'保证人名称GnrCorpName1','保证人名称置信度GnrCorpName_score1','担保描述GntDsc1','担保描述置信度GntDsc_score1',
'保证人名称GnrCorpName2','保证人名称置信度GnrCorpName_score2','担保描述GntDsc2','担保描述置信度GntDsc_score2',
'保证人名称GnrCorpName3','保证人名称置信度GnrCorpName_score3','担保描述GntDsc3','担保描述置信度GntDsc_score3',
'保证人名称GnrCorpName4','保证人名称置信度GnrCorpName_score4','担保描述GntDsc4','担保描述置信度GntDsc_score4',
'保证人名称GnrCorpName5','保证人名称置信度GnrCorpName_score5','担保描述GntDsc5','担保描述置信度GntDsc_score5',
'保证人名称GnrCorpName6','保证人名称置信度GnrCorpName_score6','担保描述GntDsc6','担保描述置信度GntDsc_score6',
'保证人名称GnrCorpName7','保证人名称置信度GnrCorpName_score7','担保描述GntDsc7','担保描述置信度GntDsc_score7',
'保证人名称GnrCorpName8','保证人名称置信度GnrCorpName_score8','担保描述GntDsc8','担保描述置信度GntDsc_score8',
'保证人名称GnrCorpName9','保证人名称置信度GnrCorpName_score9','担保描述GntDsc9','担保描述置信度GntDsc_score9',
'保证人名称GnrCorpName10','保证人名称置信度GnrCorpName_score10','担保描述GntDsc10','担保描述置信度GntDsc_score10',
#'抵押物信息列表PledgeInfoLst',
'抵质押物提供人名称MrtgCltlPrvPpL1','抵质押物提供人名称置信度MrtgCltlPrvPpL_score1','抵质押物内容描述CntntDsc1','抵质押物内容描述置信度CntntDsc_score1',
'抵质押物提供人名称MrtgCltlPrvPpL2','抵质押物提供人名称置信度MrtgCltlPrvPpL_score2','抵质押物内容描述CntntDsc2','抵质押物内容描述置信度CntntDsc_score2',
'抵质押物提供人名称MrtgCltlPrvPpL3','抵质押物提供人名称置信度MrtgCltlPrvPpL_score3','抵质押物内容描述CntntDsc3','抵质押物内容描述置信度CntntDsc_score3',
'抵质押物提供人名称MrtgCltlPrvPpL4','抵质押物提供人名称置信度MrtgCltlPrvPpL_score4','抵质押物内容描述CntntDsc4','抵质押物内容描述置信度CntntDsc_score4',
'抵质押物提供人名称MrtgCltlPrvPpL5','抵质押物提供人名称置信度MrtgCltlPrvPpL_score5','抵质押物内容描述CntntDsc5','抵质押物内容描述置信度CntntDsc_score5',
'抵质押物提供人名称MrtgCltlPrvPpL6','抵质押物提供人名称置信度MrtgCltlPrvPpL_score6','抵质押物内容描述CntntDsc6','抵质押物内容描述置信度CntntDsc_score6',
'抵质押物提供人名称MrtgCltlPrvPpL7','抵质押物提供人名称置信度MrtgCltlPrvPpL_score7','抵质押物内容描述CntntDsc7','抵质押物内容描述置信度CntntDsc_score7',
'抵质押物提供人名称MrtgCltlPrvPpL8','抵质押物提供人名称置信度MrtgCltlPrvPpL_score8','抵质押物内容描述CntntDsc8','抵质押物内容描述置信度CntntDsc_score8',
'抵质押物提供人名称MrtgCltlPrvPpL9','抵质押物提供人名称置信度MrtgCltlPrvPpL_score9','抵质押物内容描述CntntDsc9','抵质押物内容描述置信度CntntDsc_score9',
'抵质押物提供人名称MrtgCltlPrvPpL10','抵质押物提供人名称置信度MrtgCltlPrvPpL_score10','抵质押物内容描述CntntDsc10','抵质押物内容描述置信度CntntDsc_score10',
'前提条件信息列表PrmCndInfoList','保留数组信息列表KpArryInfoList',
]
list_stad_all_tag=[
'审批意见File','审批意见置信度File_score',
'授信客户名称crclntname','授信客户名称置信度crclntname_score',
'业务品种busskind1','业务品种置信度busskind1_score','标准业务品种StdBussKind1',
'币种金额描述RepymtSrc','币种金额描述置信度RepymtSrc_score',
'币种ccy4','币种置信度ccy4_score',
'单笔金额singleamt','单笔金额置信度singleamt_score',
'到期日信息描述infodsc','到期日信息描述置信度infodsc_score','标准到期日StdInfoDsc',
'期限信息描述infodsc2','期限信息描述置信度infodsc2_score','标准期限StdInfoDsc2',
'利率描述ratescop','利率描述置信度ratescop_score','利率标准StdRateScop_baserate',
'利率Xibor-StdRateScop_Xibor','利率期限StdRateScop_period', '标准利率StdRateScop_int_rate',
'利率浮动比例StdRateScop_floatrate','利率浮动XBPS-StdRateScop_floatBPS',
'受托支付信息fdcrpynm1','受托支付信息置信度fdcrpynm1_score',
'支付方式StdFdcrPyNm1_method',
'支付金额StdFdcrPyNm1_amount1',
'支付金额StdFdcrPyNm1_amount2',
'支付金额StdFdcrPyNm1_amount3',
'支付金额StdFdcrPyNm1_amount4',
'支付金额StdFdcrPyNm1_amount5',
'支付对象StdFdcrPyNm1_object1',
'支付对象StdFdcrPyNm1_object2','支付对象StdFdcrPyNm1_object3','支付对象StdFdcrPyNm1_object4','支付对象StdFdcrPyNm1_object5',
'用途usage8','用途置信度usage8_score',
'保证金描述cmdtydsc1','保证金描述置信度cmdtydsc1_score',
'保证金比例StdCmdtyDsc1_ratio', '保证金金额StdCmdtyDsc1_amount',
#'保证人信息列表GnrInfoLst',
'保证人名称GnrCorpName1','保证人名称置信度GnrCorpName_score1','担保描述GntDsc1','担保描述置信度GntDsc_score1',
'保证人名称GnrCorpName2','保证人名称置信度GnrCorpName_score2','担保描述GntDsc2','担保描述置信度GntDsc_score2',
'保证人名称GnrCorpName3','保证人名称置信度GnrCorpName_score3','担保描述GntDsc3','担保描述置信度GntDsc_score3',
'保证人名称GnrCorpName4','保证人名称置信度GnrCorpName_score4','担保描述GntDsc4','担保描述置信度GntDsc_score4',
'保证人名称GnrCorpName5','保证人名称置信度GnrCorpName_score5','担保描述GntDsc5','担保描述置信度GntDsc_score5',
'保证人名称GnrCorpName6','保证人名称置信度GnrCorpName_score6','担保描述GntDsc6','担保描述置信度GntDsc_score6',
'保证人名称GnrCorpName7','保证人名称置信度GnrCorpName_score7','担保描述GntDsc7','担保描述置信度GntDsc_score7',
'保证人名称GnrCorpName8','保证人名称置信度GnrCorpName_score8','担保描述GntDsc8','担保描述置信度GntDsc_score8',
'保证人名称GnrCorpName9','保证人名称置信度GnrCorpName_score9','担保描述GntDsc9','担保描述置信度GntDsc_score9',
'保证人名称GnrCorpName10','保证人名称置信度GnrCorpName_score10','担保描述GntDsc10','担保描述置信度GntDsc_score10',
#'抵押物信息列表PledgeInfoLst',
'抵质押物提供人名称MrtgCltlPrvPpL1','抵质押物提供人名称置信度MrtgCltlPrvPpL_score1','抵质押物内容描述CntntDsc1','抵质押物内容描述置信度CntntDsc_score1',
'抵质押物提供人名称MrtgCltlPrvPpL2','抵质押物提供人名称置信度MrtgCltlPrvPpL_score2','抵质押物内容描述CntntDsc2','抵质押物内容描述置信度CntntDsc_score2',
'抵质押物提供人名称MrtgCltlPrvPpL3','抵质押物提供人名称置信度MrtgCltlPrvPpL_score3','抵质押物内容描述CntntDsc3','抵质押物内容描述置信度CntntDsc_score3',
'抵质押物提供人名称MrtgCltlPrvPpL4','抵质押物提供人名称置信度MrtgCltlPrvPpL_score4','抵质押物内容描述CntntDsc4','抵质押物内容描述置信度CntntDsc_score4',
'抵质押物提供人名称MrtgCltlPrvPpL5','抵质押物提供人名称置信度MrtgCltlPrvPpL_score5','抵质押物内容描述CntntDsc5','抵质押物内容描述置信度CntntDsc_score5',
'抵质押物提供人名称MrtgCltlPrvPpL6','抵质押物提供人名称置信度MrtgCltlPrvPpL_score6','抵质押物内容描述CntntDsc6','抵质押物内容描述置信度CntntDsc_score6',
'抵质押物提供人名称MrtgCltlPrvPpL7','抵质押物提供人名称置信度MrtgCltlPrvPpL_score7','抵质押物内容描述CntntDsc7','抵质押物内容描述置信度CntntDsc_score7',
'抵质押物提供人名称MrtgCltlPrvPpL8','抵质押物提供人名称置信度MrtgCltlPrvPpL_score8','抵质押物内容描述CntntDsc8','抵质押物内容描述置信度CntntDsc_score8',
'抵质押物提供人名称MrtgCltlPrvPpL9','抵质押物提供人名称置信度MrtgCltlPrvPpL_score9','抵质押物内容描述CntntDsc9','抵质押物内容描述置信度CntntDsc_score9',
'抵质押物提供人名称MrtgCltlPrvPpL10','抵质押物提供人名称置信度MrtgCltlPrvPpL_score10','抵质押物内容描述CntntDsc10','抵质押物内容描述置信度CntntDsc_score10',
'前提条件信息列表PrmCndInfoList','保留数组信息列表KpArryInfoList',
]
bracket_map = {"(": ")", "[": "]", "{": "}", "（": '）'}
bracket_map_1 = {i: j for j, i in bracket_map.items()}
open_par = ["(", "[", "{", '（']  # 使用集合降低时间复杂度
open_par_1 = [']', '}', ")", '）']
open_par_2 =["(", "[", "{", '（', ']', '}', ")", '）']

run_app_result_dict = {"CrClntName": "", "CrClntName_score": "", "BussKind1": "", "BussKind1_score": "", "RepymtSrc": "", "RepymtSrc_score": "", "Ccy4": "", "Ccy4_score": "", "InfoDsc": "", "InfoDsc_score": "", "InfoDsc2": "", "InfoDsc2_score": "", "RateScop": "", "RateScop_score": "", "StdRateScop_baserate": "", "StdRateScop_Xibor": "", "StdRateScop_period": "", "StdRateScop_int_rate": "", "StdRateScop_floatrate": "", "StdRateScop_floatBPS": "", "FdcrPyNm1": "", "FdcrPyNm1_score": "", "StdFdcrPyNm1_method": "", "StdFdcrPyNm1_amount": "", "StdFdcrPyNm1_object": "", "Usage8": "", "Usage8_score": "", "CmdtyDsc1": "", "CmdtyDsc1_score": "", "StdCmdtyDsc1_ratio": "", "StdCmdtyDsc1_amount": "", "GnrInfoLst": [], "PledgeInfoLst": [], "SingleAmt": "", "SingleAmt_score": "", "StdInfoDsc": "", "StdInfoDsc2": "", "StdBussKind1": ""}