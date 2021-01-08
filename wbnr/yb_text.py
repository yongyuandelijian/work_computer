# 功能：获取文档固定文本部分，按照章节情况将内容保存到一个字典中
# date:20200723
# author:aaa

class get_ybwb(object):
    '''获取文档固定文本部分，按照章节情况将内容保存到一个字典中'''
    def hqnr(self):
        '''获取文档固定文本部分，按照章节情况将内容保存到一个字典中'''
        yj1 = "第1章\t概述\t\t"
        # nr1_01 = ""
        # yj1={yj1,nr1_01}
        ej11 = "1.1\t编写目的\t\t"
        nr11_01 = "云平台数据管理子项目在实施的过程中需要将各单位分发库的数据集成到云平台中，在实际数据集成的过程中存在各种各样的问题，如分发库的OGG进程中断、分发库的重建、数据集成抽取任务的失败等，本文档就数据集中链路过程中存在的问题进行相应的说明及描述。"
        ej11 = {ej11: [nr11_01]}
        ej12 = "1.2\t阅读对象\t\t"
        nr12_01 = "云平台数据管理子项目人员。"
        ej12 = {ej12: [nr12_01]}
        ejt1 = (ej11, ej12)

        # 第二章这里是三层标题外加内容，循环里要单独判断,而且这一块内容可能会随着业务增加会有变动,这块后期需要确认最好可以维护在表里面，这样获取到直接按维护的内容生成，也就不需要写这么多内容了
        yj2 = "第2章\t数据集中链路现状\t\t"
        nr2 = "目前总局云平台数据采集链路及分层架构，基于目前总局、省级单位相关税收业务数据、外部交换数据、出口退税、电子底账和互联网采集等数据的分布特性，云平台目前共有10条数据集成链路，根据不同的数据来源，我们采用相对应的技术工具，将不同位置不同业务的数据源数据首先采集至云平台各项目独立存储区即镜像层，再按需同步至国税总局基础层，个别临时提供的数据直接集成到国税总局基础层，最终实现云平台基础数据层数据的采集。如上图所示：各省局单位在云平台有自己对应的镜像/临时层项目空间，总局数据大部分在统一的总局镜像层项目空间，其它各专项需求数据也有自己对应单独镜像层项目空间，每部分数据原则上首先是进入云平台镜像层，再按需进入下游。下面分别说明各链路："
        ej21 = "2.1\t省级单位数据源（36家）集成链路\t\t"
        sj21_01="2.1.1\t链路1：金三核心征管、个税及电子税务局数据集成"
        nr21_01="主要包含了核心征管、个人税收管理（主要为地税）、工作流应用、日志数据及省局电子税务局等生产型业务数据，此链路中其中核心征管及个税数据是从源端生产库将数据通过OGG同步到各地核心征管分发库中，云平台再通过在个单位分发库部署的OGG工具以增量形式将数据集成到云平台，每日增量数据进入云平台各单位临时层，再merge到云平台基础层供下游使用；省局电子税务局数据主要包含系统用户身份、行为痕迹、审批流程、征管服务调用等数据由云平台直接从各单位抽取到云平台各单位镜像层中，目前下游未使用此部分数据；"
        sj21_01={sj21_01:nr21_01}
        ej21={ej21:[sj21_01]}
        ej22 = "2.2\t总局数据源集成链路\t\t"
        sj22_01 = "2.2.1\t链路2：出口退税数据集成"
        nr22_01="针对出口退税系统目前由大连龙图每月月初将原系统数据推送到总局出口退税中间库，再由云平台月调度任务全量抽取到国税总局镜像层，由镜像层再同步到基础层供下游使用；"
        sj22_01={sj22_01:nr22_01}
        sj22_02 = "2.2.2\t链路3：发票底账数据集成"
        nr22_02="针对发票底账数据由长软每日以增量方式将数据推送至总局一包电子底账库，主要涉及增值税普通发票，专票，电子发票，卷式发票；货运普通发票，专票，电子发票，卷式发票；发票认证信息；机动车发票等数据，云平台每日进行增量方式采集集成到云平台国税总局镜像层，再merge到基础层供下游使用；"
        sj22_02={sj22_02:nr22_02}
        sj22_03 = "2.2.3\t链路4：外部交换数据集成"
        nr22_03="针对总局外部交换集中的海关、工商、人民银行、外汇局、银监会、代码中心、中机中心，银保监会、建行、发改委、最高法11个第三方部门的数据进行采集集成，此部分数据均是以按日增量方式先集成到总局镜像层，再按需同步到基础层供下游使用；"
        sj22_03={sj22_03:nr22_03}
        sj22_04 = "2.2.4\t链路5：总局二包风险及信用相关数据集成"
        nr22_04 ="针对总局决策二包集中的企业纳税信用评级数据、风险管理、风险情报、风险信用等数据按需进行采集集成，有按周、按日、按月三种频率进行集成；"
        sj22_04={sj22_04:nr22_04}
        sj22_05 = "2.2.5\t链路6：互联网爬取数据集成"
        nr22_05="以总局为节点采集政府公开公示、企业官网以及财经新闻门户等互联网信息，集成后进行结构化再集成到云平台镜像层，按需同步到基础层供下游使用，此类数据为按需集成；"
        sj22_05={sj22_05:nr22_05}
        sj22_06 = "2.2.6\t链路7：协同办公平台数据集成"
        nr22_06 = "主集成了总局协同办公平台系统的异常抵扣数据，此部分数据由源端推送到决策一包，云平台从决策一包按周抽取；"
        sj22_06 = {sj22_06: nr22_06}
        sj22_07 = "2.2.7\t链路8：总局其它系统数据"
        nr22_07 = "主要包括总局统一工作平台用户权限岗位等数据及基于云平台开发的应用增值税发票风险监控系统产生的数据，此部分数据均是按日集成；"
        sj22_07 = {sj22_07: nr22_07}
        sj22_08 = "2.2.8\t链路9：外部临时导出数据集成"
        nr22_08 ="针对一些临时需求从外部其它系统临时导出的相关数据进行云平台集成，如公安的自然人身份信息数据，海关的注册企业信息等，此部分数据经常以文件形式提供，单次按需集成，所有数据均直接进入云平台基础层，供下游直接加工使用；"
        sj22_08={sj22_08:nr22_08}
        sj22_09 = "2.2.9\t链路10：老核心征管系统历史数据集成"
        nr22_09="针对总局电税中心留存的核心管理历史数据（CTAIS1.1、2.0）进行采集集成，此部分数据也是独立需求，在云平台做为独立项目进行数据分析使用，因此数据存放于自己独立镜像层下进行加工分析使用；"
        sj22_09={sj22_09:nr22_09}
        sj22_10 = "2.2.10\t链路11：罗格电子商务数据集成"
        nr22_10 = "针对罗格公司的电子商务相关各类数据进行采集并在云平台进行分析利用，此部分数据也是作为一个专项需求进行使用，因此数据存放于云平台独立镜像层，在镜像层进行整合后按需同步到国税总局基础层与税务数据综合起来使用；"
        sj22_10={sj22_10:nr22_10}
        sj22_11 = "2.2.11\t链路12：所得税汇算清缴系统数据集成"
        nr22_11="针对总局所得税司所得税汇算清缴系统，涉及两部分数据，一个是所得税汇总纳税相关数据，一个是所得税汇算清缴相关数据进行采集集成，此部分数据是也作为独立需求进行分析使用，因此在云平台存于自己单独的镜像层下，按需分析利用。"
        sj22_11 = {sj22_11: nr22_11}
        sj22_12 = "2.2.12\t链路13：ITS系统个税数据集成"
        nr22_12 = "此部分数据来自总局个税管理系统，目前按天抽取集成，按需从ITS系统采集，由于此部分数据安全保密要求较高，进入云平台后配置单独项目空间存储，与公共基础层分开独立开发使用。"
        sj22_12 = {sj22_12: nr22_12}

        zj_2="以上为云平台数据采集链路介绍，云平台将数据采集上来后总体原则是按需同步到基础层，再将基础层的数据加工到中间层，模型层利用中间层加工的结果进行数据模型设计分析。"
        ej22 = {ej22: [sj22_01,sj22_02,sj22_03,sj22_04,sj22_05,sj22_06,sj22_07,sj22_08,sj22_09,sj22_10,sj22_11,sj22_12]}
        ejt2 = (ej21, ej22)

        yj3 = "第3章\t源端链路运行监控\t\t"
        nr3="源端链路包括省局数据源跟总局数据源链路两部分。总局主要是出口退税、电子底账、外部交换、总局一包、二包等数据源，目前总局数据源由于集成的数据表相对于省局比较少，并且总局数据源由各厂商驻场运维，一旦接入云平台数据集成链路，源端数据链路运行会优先及时保障，极少出现异常情况，因此总局数据源链路运行情况在云平台端未进行日常性监控。省局主要是各单位分发库数据源，由于此链路同步大量核心征管及个税的数据，是比较核心重要的链路，针对各单位分发库运行情况，我们在云平台端开发了OGG进程运行监控工具辅助进行源端链路监控。下面重点说明省局数据源链路运行的监控情况：\n"
        ej31 = "3.1\t分发库概述\t\t"
        nr31_01 = "目前国地税合并后全国共有36个分发库，分发库全部部署在各地方单位。在整个数据集中链路中，分发库相当于是云平台的源端，各省数据通过前台汇总至核心征管库后，通过OGG生成同步至分发库；在分发库服务器端部署针对云平台集成相关的ogg工具及数据打包传输工具，分钟级执行，生成增量数据文件，云平台按日获取增量数据文件进行集成。"
        ej31 = {ej31: [nr31_01]}
        ej32 = "3.2\t分发库运行情况\t\t"
        nr32_01 = "分发库运行情况通过OGG链路监控工具每天对全国36家单位分发库OGG链路运行巡检，对于各进程运行情况进行实时监控。本月每日运维监控各单位分发库链路或OGG进程异常情况统计如下："
        ej32 = {ej32: [nr32_01]}
        ej33 = "3.3\t分发库异常分析\t\t"
        nr33_01 = "针对各单位异常情况进行了跟踪分析，具体如下："
        ej33 = {ej33: [nr33_01]}
        ej34 = "3.4\t分发库异常应对策略\t\t"
        nr34_01 = "针对分发库各类原因导致的进程异常问题，可采取以下办法应对："
        nr34_02 = "1、人为导致的未刷新定义文件处理如下："
        nr34_03="停止复制进程，开始执行ggsrun.sh脚本实现定义文件刷新；执行成功后重启相关的ogg进程即可。"
        ej34 = {ej34: [nr34_01, nr34_02,nr34_03]}
        ejt3 = (ej31, ej32, ej33, ej34)

        yj4 = "第4章\t云平台数据集成\t\t"
        ej41 = "4.1\t云平台数据集成概述\t\t"
        nr41_01 = "云平台数据集成情况如下表所示，具体说明如下："
        nr41_04 = "3、目前数据抽取统一采用数据交换工具DataX将数据按频度（日/月）、增/全量方式抽取到云平台镜像层，再根据下游应用需求集成到基础层。"
        nr41_05 = "4、核心征管及个税所有表目前采用增量文件的方式从分发库按日进行采集集成，最终合并到基础层；"
        nr41_06 = "5、增量方式抽取的表先将数据抽取到临时层，再与上一天镜像层的全量进行合并成当天全量到镜像层，再按需同步到基础层供下游使用；"
        nr41_07 = "6、 核心征管、个税系统、发票底帐，外部交换系统、风险管理系统的表每天0点开始将T-1日数据抽取到镜像层；风险过程、出口退税数据每月10号将上个月数据抽取到镜像层；决策二包信用评级数据每周一全量抽取集成到基础层。"
        nr41_08 = "7、互联网、风险过程、千户集团、电子商务和决一营改增分析这五部分数据根据需求按次集成；老的征管历史数据、所得税汇算清缴数据、所得税汇总纳税数据、收规处社保数据、宁波各部门个税测算数据、公安自然人身份信息数据及风险司海关注册企业信息数据是单次集成到云平台，以后无需再集成；"
        nr41_09 = "8、云平台的数据采用切片方式进行存储，每个切片都是一个系统的全量数据。镜像层采用一级分区，其中核心征管、个税系统、发票底账、外部交换均采用日分区，出口退税、纳税信用评级数据采用月分区；基础层采用两级分区，除了日/月分区外还有数据所属地区分区（注：日分区的日期为业务日期即该笔业务发生的日期而非自然日期）。"
        nr41_10 = "9、云平台镜像和基础层数据由38个项目组成，分别是36家省级镜像层、1家总局镜像层、1家总局基础层，其中镜像层数据保持贴源，设计基础层的目的是用来标准化清洗数据。"
        ej41 = {ej41: [nr41_01,nr41_04,nr41_05,nr41_06,nr41_07,nr41_08,nr41_09,nr41_10]}
        ej42 = "4.2\t数据集成任务情况\t\t"
        nr42_01="本月云平台集成任务运行相对平稳良好。"
        ej42 = {ej42: [nr42_01]}
        ej43 = "4.3\t运行失败任务分析\t\t"
        nr43_01 = "从运维监控到的失败任务暴露出的问题来看归纳统计如下："
        ej43 = {ej43: [nr43_01]}
        ej44 = "4.4\t失败任务应对策略\t\t"
        nr44_01 = "\n"
        nr44_02="\n"
        ej44 = {ej44: [nr44_01,nr44_02]}
        ej45 = "4.5\t数据集成一致性监控处理情况\t\t"
        nr45_01="目前云平台数据集成基本都采用datax工具进行任务自动集成，除了核心征管及个税系统数据采用增量文件加载到云平台集成以外，其它系统数据均是通过jdbc直接从源端库抽取到云平台的，全量抽取的这部分数据一致性不会存在异常问题，无需比对，增量抽取的由于表数量较少，数据使用频率不是很高，一般是定期抽样进行差异比对。核心征管与个税数据由于抽取的表数量比较多，且全部是增量抽取，数据使用比较广泛，因此此部分数据一致性比对是纳税日常运维工作当中的，增量抽取过程相对复杂，在数据从源端库到云平台同步时存在很多不可控因素，比如源端库数据版本升级不规范等，端与端之间网络不稳定等等，难免导致同步到目标端的数据与源端数据存在一定的不一致性，针对这种不一致性我们采取数据量的比对措施进行验证，以此来证明源库与目标库数据量一致，数据在集成过程当中没有存在丢失。"
        nr45_02="统计附件Excel1个\nExcel备注说明：\n分发库——同步任务启动时分发库此表数据量；\n基础层——同步任务结果后基础层此表当天分区数据量\n差异——此表分发库数据量与当天分区基础层数据量的差\n即：差异=分发库-基础层\n差异率——此表分发库数据量与当天分区基础层数据量的差比副本库\n即：差异率=（分发库-基础层）/分发库*100%"
        nr45_03="由此数据量比对结果可看出，数据同步基本稳定，无差异较大情况，由于统计分发库数据量的任务启动时间为每日零点启动，但是任务需要运行10分钟左右（个别单位由于资源问题运行的时间会更长），所以导致统计到的分发库的数据量比实际当天的数据量要多一些，这种情况会通过和第二天的增量进行比较来排除出去，剩下的数据存在差异的表会通过全量初始化的方式来保障数据的完整性。云平台每日对各单位各表数据量比对有所监控，差异率在0.01%（含）及以上的我们当天将会对此表进行全量初始化来补全数据。此次比对结果中是空值的是因为该单位统计该表的数据量的任务卡死，导致获取不到该表数据量，所以该单位分发库数据量值为空，这种表无法进行后续的数据比对，是通过比对云平台中该表的数据趋势来判断该表是否需要处理。以下为本月运维和数据差异的处理记录，详情见附件：\nExcel表格1个"
        ej45={ej45:[nr45_01,nr45_02,nr45_03]}
        ej46="4.6\t源端数据更新情况\t\t"
        ej46_01="备注说明：云平台数据未更新的表在源端数据库中无数据变化。"
        ej46={ej46:[ej46_01]}
        ejt4 = (ej41, ej42, ej43, ej44,ej45,ej46)


        yj5 = "第5章\t总结与建议\t\t"
        ej51 = "5.1\t副本库\t\t"
        nr51_01 = "基于上述分析，分发库存在的问题有分发库密码过期导致的异常，分发库运维人员操作不规范导致的集成问题，OGG进程异常问题等。对于上述问题的建议解决方案有以下三点："
        nr51_02 = "（1）各地分发库关于数据集成相关的用户密码或者当地安全策略如有变动，请第一时间告知云平台，否则会导致云平台数据集成延时。"
        nr51_03 = "（2）各单位加强运维管理，对OGG相关的问题处理严格按照云平台提供的规范文档进行处理并保存自己的操作记录，避免出现不必要的错误。"
        nr51_04 ="（3）各地如存在非常规操作，应事先通知云平台工作人员，以便云平台对任务进行处理。例如全表的全量初始化操作，对云平台增量任务的压力较大，很容易造成数据积压，导致该单位的数据集成任务延迟。"
        ej51 = {ej51: [nr51_01, nr51_02,nr51_03,nr51_04]}
        ej52 = "5.2\t云平台数据集成\t\t"
        nr52_01 = "目前云平台运行基本稳定，存在的问题不是很多，本月出现错误的任务也不多并且问题的错误类型相对集中，大部分的错误都是由于当地人员操作的方式不规范及云平台扩容导致的任务出错。上述的问题可以通过以下方法解决："
        nr52_02 = "（1）对于脏数据问题，需要当地运维人员严格按照云平台提供的运维规范对附加日志进行操作。"
        nr52_03="（2）平台原因导致的异常，例如实例调度失败、IO异常、安全策略不通等，有问题再联系阿里解决后再重跑即可。"
        ej52 = {ej52: [nr52_01, nr52_02,nr52_03]}
        ejt5 = (ej51, ej52)
        yj6="第6章\t附件\t\t"
        ejt6=()
        ml = {
            yj1: ejt1,
            yj2: ejt2,
            yj3: ejt3,
            yj4: ejt4,
            yj5: ejt5,
            yj6: ejt6
        }

        return ml,nr2,nr3,zj_2