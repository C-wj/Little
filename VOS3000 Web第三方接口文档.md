**资料编码**
**VOS****3000**
**V**
**Web ****接口说明书**
**文档版本**     **05**
**发布日期**     **2022-10-19**
**昆石网络技术有限公司**
**版权所有** **®  ****昆石网络技术有限公司** **2022****。** **保留一切权利。**
非经本公司书面许可，任何单位和个人不得擅自摘抄、复制本文档内容的部分或全部，并不得以任何形式传 播。
**商标声明**
和其他昆石商标均为昆石网络技术有限公司的商标。
本文档提及的其他所有商标或注册商标，由各自的所有人拥有。
**注意**
您购买的产品、服务或特性等应受昆石公司商业合同和条款的约束，本文档中描述的全部或部分产品、服务 或特性可能不在您的购买或使用范围之内。除非合同另有约定，昆石公司对本文档内容不做任何明示或暗示 的声明或保证。
由于产品版本升级或其他原因，本文档内容会不定期进行更新。除非另有约定，本文档仅作为使用指导，本 文档中的所有陈述、信息和建议不构成任何明示或暗示的担保。
昆石网络技术有限公司
网址：
**目**  **录**
**	****1 ****概述**
本文档描述在昆石 VOS3000 标准接口。部分接口需购买特定功能组件才可实施，请在使用接口时核 实您安装的产品具备该功能。
接口综述:
l     接口格式采用 JSON 定义，采用UTF-8 格式编码
l     接口采用 POST 方式提交至 VOS3000 WEB 服务
l     对于接口返回码，非 0 表示失败。失败原因参考返回码定义
l     HTML  头部信息 Content-Type  设置为 text/html;charset=UTF-8
l     一般返回错误格式样例{"retCode":-10007,"exception":"Not found, operation failed."}
l     对于有性能以及压力要求的接口请求，建议安排相同机器环境，测试后方可实际环 境部署。
**	****2**** ****配置**
2.1 接入配置
位置：接口管理-Web 访问控制
l     Web 服务器设备：设备名称
l      目录名称：允许访问的接口目录范围
n    /external/server：正式接口
n    /external/server/GetCustomer：细化具体接口使用范围-查询账户
n    /external/test/server：浏览器可视化调试界面
l     允许接入 IP：访问接口时使用的 IP 地址 l      备注
2.2 接口地址
端口/目录名称
端口/目录名称
2.3 调试界面
当接口完成部署，您可以根据以下链接或咨询技术供应商进行配置与调试
https://www.linknat.com/#/support/faqdetail/33
每个接受请求接口都准备了测试页面供调用参考。
可测试接口汇总页面
测试接口交互格式样例
**3 ****功能操作**
表格头域说明
l     必须: M  表示必填字段 O 表示可选字段
l      类型:
n    String 表示长度为255 以内的字符串
n    LongString 表示长度为 65535 以内的字符串
n    其余类型定义遵照 Java 基础类型定义
3.1 创建账户
接口地址/external/server/CreateCustomer
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码（具备唯一性的可显标识） |
| name | M | String | 账户名称 |
| money | O | Double | 开户初始余额（默认:0） |
| limitMoney | O | Double | 开户初始透支限额（默认:0） |
| feeRateGroup | O | String | 计费费率 |
| type | O | Integer | 账户类型 0:普通账户（默认） 1:电话卡 2:结算账户 |
| lockType | O | Integer | 锁定类型 0:未锁定（默认） 1:锁定 |
| agentAccount | O | String | 代理商账号 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| phoneBookLimit | O | Integer | 电话簿上限（默认:0） |
| validTime | O | Long | 账户有效期（UTC 1970-01-01 至今 的毫秒数） 0:使用系统参数决定的过期时间 |
| ctdBillingType | O | Integer | 代理商回拨计费模式 0:普通（默认） 1:流量 |
| memo | O | String | 备注信息 |
| infoCustomerAdditional | O | InfoCustomerAdditional | 账户补充信息 |

InfoCustomerAdditional 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| cardType | O | Integer | 证件类型 0:身份证（默认） 1:护照 2:军官证 3:工作证 4:学生证 5:其他证件 |
| cardNumber | O | String | 证件号码 |
| address | O | String | 地址 |
| postCode | O | String | 邮政编码 |
| linkMan | O | String | 联系人 |
| telephone | O | String | 电话号码 |
| fax | O | String | 传真 |
| email | O | String | 邮件地址 |
| emailCc | O | String | 抄送地址 |
| emailBcc | O | String | 密送地址 |
| reportType | O | Integer | 报表发送类型 0:不发送（默认） 1:每日 2:每周 3:每月 |
| companyName | O | String | 公司名称 |
| bank | O | String | 银行名称 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.2 修改账户
接口地址/external/server/ModifyCustomer
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码（具备唯一性的可显标识） |
| name | O | String | 账户名称 |
| limitMoney | O | Double | 开户初始透支限额（默认:0） |
| feeRateGroup | O | String | 计费费率 |
| type | O | Integer | 账户类型 0:普通账户（默认） 1:电话卡 2:结算账户 |
| lockType | O | Integer | 锁定类型 0:未锁定（默认） 1:锁定 |
| agentAccount | O | String | 代理商账号 |
| phoneBookLimit | O | Integer | 电话簿上限（默认:0） |
| validTime | O | Long | 账户有效期（UTC 1970-01-01 至今 的毫秒数） |
| ctdBillingType | O | Integer | 代理商回拨计费模式 0:普通 1:流量 |
| memo | O | String | 备注信息 |
| infoCustomerAdditional | O | InfoCustomerAdditional | 账户补充信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.3 删除账户
接口地址/external/server/DeleteCustomer
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 计费账户号码（具备唯一性的可显 标识） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.4 查询账户
接口地址/external/server/GetCustomer
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| accounts | O | String[] | 账 户 号 码 列 表 （与 e164s 、 filterAgentAccount  三 项至少选其 一） |
| e164s | O | String[] | 电话号码列表 |
| filterAgentAccount | O | FilterAgentAccount | 代理商账户（表示仅查询该代理商 的下属账户） |
| type | O | Integer | 账户类型 0:普通账户 1:电话卡 2:结算账户 |

FilterAgentAccount  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| filterAgentAccount | M | String | 代理商账户号码 |
| querySonMode | M | int | 0:所有下属账户 1:直属下属账户 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoCustomers | O | InfoCustomer[] | 账户信息 |

InfoCustomer  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码（具备唯一性的可显标识） |
| name | M | String | 账户名称 |
| money | M | double | 开户初始余额（默认:0） |
| limitMoney | M | double | 开户初始透支限额（默认:0） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| feeRateGroup | M | String | 计费费率 空串:无费率组 |
| type | M | int | 账户类型 0:普通账户（默认） 1:电话卡 2:结算账户 |
| lockType | M | int | 锁定类型 0:未锁定（默认） 1:锁定 |
| agentAccount | M | String | 代理商账号 空串:无代理商 |
| phoneBookLimit | M | int | 电话簿上限（默认:0） |
| canceled | M | boolean | true:已注销 false:未注销 |
| startTime | M | long | 账户有效期（UTC 1970-01-01 至今 的毫秒数） 0:使用系统参数决定的过期时间 |
| validTime | M | long | 账户有效期（UTC 1970-01-01 至今 的毫秒数） 0:使用系统参数决定的过期时间 |
| todayConsumption | M | double | 今日消费 |
| ctdBillingType | M | int | 代理商回拨计费模式 0:普通 1:流量 |
| category | M | int | 账户类别 0:普通账户 1:代理商账户 |
| bindedE164s | M | String [] | 绑定号码列表 |
| memo | M | String | 备注信息 |
| infoCustomerAdditional | M | InfoCustomerAdditional | 账户补充信息 |

3.5 查询所有账户
/external/server/GetAllCustomers
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| Key | O | integer | 查询所有账户 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| accounts | O | String | 所有账户名称 |

3.6 创建话机
接口地址/external/server/CreatePhone
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| autoCreateAccount | M | boolean | 创建话机时同时创建计费账户 |
| e164 | M | String | 话机号码 |
| account | O | String | 话机所属账户 |
| password | O | String | 话机密码 |
| displayNumber | O | String | 去电显示 |
| lockType | O | Integer | 锁定类型 0:无锁定 1:锁定呼出 2:锁定呼入 3:全部锁定 |
| callLevel | O | Integer | 权限类型 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| feerateGroup | O | String | 话机私有计费费率（请参考操作手 册费率相关描述）通常情况不使用 此设置 |
| monthlyMoneyMinimum | O | Double | 月最低消费额 |
| monthlyMoneyMaximum | O | Double | 月最高消费额 |
| monthlyRentFee | O | Double | 月租 |
| rewriteRulesOutCallee | O | LongString | 呼出被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCallee | O | LongString | 呼入被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCaller | O | LongString | 呼入主叫拨号规则，需符合拨号规 则书写格式 |
| routingGatewayGroupsAll ow | O | Boolean | true:仅允许设定的网关群组作为落 地 false:禁止设定的网关群组作为落地 |
| routingGatewayGroups | O | String | 落地网关群组名称（空表示所有） |
| equipment | O | String | 话机所属软交换（空表示属于所有 软交换） |
| calleeBilling | O | Boolean | true:开启被叫计费 false:普通计费（主叫计费） |
| customerPassword | O | String | Web 查询密码 |
| lineCallIn | O | Integer | 呼入线路数量限制 |
| lineCallOut | O | Integer | 呼出数量限制 |
| lineCapacity | O | Integer | 同时呼叫数限制（含呼入与呼出） |
| phonebookLimit | O | Integer | 电话簿数量限制 |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许主叫号码组呼入 false:禁止主叫号码组呼入 |
| callerLimitE164Groups | O | String | 当话机为被叫时 允许/禁止的主叫 号码组（空表示所有） |
| calleeLimitE164Allow | O | Boolean | true:允许呼出的被叫号码组 false:禁止呼出的被叫号码组 |
| calleeLimitE164Groups | O | String | 当话机为主叫时 允许/禁止的被叫 号码组（空表示所有） |
| dids | O | String | 一机多号 |
| memo | O | String | 备注 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| infoPhoneValueAdded | O | InfoPhoneValueAdded | 话机增值业务 |
| infoPhoneAdditional | O | InfoPhoneAdditional | 话机补充设置 |

InfoPhoneValueAdded 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerIdDisplay | O | Boolean | true:开启来电显示 false:关闭来电显示 |
| callTransfer | O | Boolean | true:允许呼叫转移 false:禁止呼叫转移 |
| doNotDisturb | O | Boolean | true:开启免打扰 false:关闭免打扰 |
| periodForwarding | O | Boolean | true:开启时段前转 false:关闭时段前转 |
| infoPhoneValueAddedPeri odForwardings | O | InfoPhoneValueAddedPeri odForwarding[] | 时段转移设置 |
| unconditionalForward | O | Boolean | true:开启无条件前转 false:关闭无条件前转 |
| unconditionalForwardE164 | O | InfoPhoneValueAddedFor wardE164 | 无条件前转号码 |
| noAnswerForward | O | Boolean | true:开启无应答前转 false:关闭无应答前转 |
| noAnswerForwardE164 | O | InfoPhoneValueAddedFor wardE164 | 无应答前转号码 |
| offlineForward | O | Boolean | true:开启不在线前转 false:关闭不在线前转 |
| offlineForwardE164 | O | InfoPhoneValueAddedFor wardE164 | 不在线前转号码 |
| busyForward | O | Boolean | true:开启遇忙前转 false:关闭遇忙前转 |
| busyForwardE164 | O | InfoPhoneValueAddedFor wardE164 | 遇忙前转号码 |
| callForwardDisplay | O | Integer | 呼叫前转去电显示 0:默认，使用系统参数值 1:原始主叫 2:本机号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callTransferNormalDisplay | O | Integer | 普通呼叫转移去电显示 0:默认，使用系统参数值 1:原始主叫 2:本机号码 |
| callTransferAskDisplay | O | Integer | 询问式呼叫转移去电显示 0:默认，使用系统参数值 1:原始主叫 2:本机号码 |
| colorRing | O | Boolean | true:开启彩铃 false:关闭彩铃 |
| remoteColorRingPassthrou gh | O | Boolean | true:开启彩铃透传 false:关闭彩铃透传 |
| colorRingName | O | String | 彩铃名称 |
| language | O | String | 无法接通语音提示/余额不足语音 提示/通话剩余时长插播 使用的语 言 |
| unableToConnectVoicePro mpts | O | Integer | 无法接通语音提示 0:默认，使用系统参数值 1:开启 2:关闭 |
| callRemainingTimePrompt s | O | Integer | 通话剩余时长插播 0:默认，使用系统参数值 1:提示剩余金额 2:提示剩余分钟数 3:不进行提示 |
| balanceNotEnoughAlarm | O | Integer | 余额不足语音提示 0:默认，使用系统参数值 1:开启 2:关闭 |
| voiceMail | O | Boolean | true:语音信箱开通 false:语音信箱关闭 |
| voiceMailCheckPassword | O | Boolean | true:接入语音信箱校验密码 false:接入语音信箱不校验密码 |
| voiceMailMaxNumber | O | Integer | 语音信箱保留的条数 -1:由系统参数决定 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| voiceMailExpireDay | O | Integer | 语音信箱留言过期天数 -1:由系统参数决定 |
| voiceMailAudioType | O | Integer | 0:默认 1:自定义 |

InfoPhoneValueAddedPeriodForwarding 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| weekOfDay | O | String | 星期几生效设定，可使用逗号分隔 多个生效天如 0,1 不设置默认为 0,1,2,3,4,5,6 0:星期日 1:星期一 2:星期二 3:星期三 4:星期四 5:星期五 6:星期六 全星期生效可设置为 0,1,2,3,4,5,6 |
| beginSecondInDay | O | Integer | 起始时间（当前时间与当天 0 点的 秒偏差） 不设置默认为 0 取值范围 0-86400 |
| endSecondInDay | O | Integer | 终止时间（当前时间与当天 0 点的 秒偏差） 不设置默认为 86400 取值范围 0-86400 |
| forwardE164 | O | InfoPhoneValueAddedFor wardE164 | 前转号码 |

InfoPhoneValueAddedForwardE164 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| forwardMethod | O | Integer | 前转方式，不设置则默认为 0 0:顺序 2:随机 3:同振 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| alertSecond | O | Integer | 前转后振铃时长（单位:秒），对最 后一个前转号码无效 不设置默认为-1 -1:使用默认值 |
| e164 | O | String | 前转号码， 可使用逗号分隔多个号 码 |

InfoPhoneAdditional 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| registerType | O | Integer | 注册方式 0:静态 1:动态 2:对接网关 |
| protocol | O | Integer | 协议 0:H323 1:SIP |
| ip | O | String | 静态注册方式时的 IP 地址 |
| port | O | Integer | 静态注册方式时的端口 |
| localIp | O | String | 静态注册方式时使用的本地IP 地址 |
| rtpRelay | O | Integer | 媒体转发 0:自动 1:开启 2:关闭 3:必须开启 |
| rtpInterruptDetection | O | Integer | 媒体中断监测 0:无 1:服务器至远端 2:远端至服务器 3:双向 |
| callDurationLimit | O | Integer | 通话时长限制（单位:秒） -1:默认，使用系统参数设置值 0:无，不限制通话时长 |
| useCallerPhoneDisplay | O | Integer | 非电话簿主叫话机使用其去电显示 0:默认，使用系统参数设置值 1:开启 2:关闭 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| noBillingToPhone | O | Integer | 当对方是话机设备时免计费 0:默认，使用系统参数设置值 1:开启 2:关闭 |
| displayCallerShortNumber | O | Boolean | true:显示主叫短号 false:不显示主叫短号 |
| useRoutingGatewayNotOn line | O | Integer | 不在线尝试落地网关路由 0:默认，使用系统参数设置值 1:开启 2:关闭 |
| minProfitPercentEnable | O | Boolean | 是否开启最低利润率限制 |
| minProfitPercent | O | Integer | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | O | Boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | O | Double | 最高秒费率值（若分钟费率为 0.6， 此值应该设置为 0.01） |
| firstRoutingPolicy | O | Integer | 第一路由策略 0:无 1:接通率 2:最少秒费率 |
| secondRoutingPolicy | O | Integer | 第二路由策略 0:无 1:接通率 2:最少秒费率 |
| sipAuthenticationMethod | O | Integer | SIP 呼叫时认证方式 0:根据 IP 地址 1:根据 IP 地址和端口 |
| sipRemoteAlertingMethod | O | Integer | 远端回铃方式 0:透传 1:183+SDP 2:180+SDP |
| sipTimerSupport | O | Boolean | true:允许 timer 协议（RFC4028） false:禁止 timer 协议 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sip100RelSupport | O | Boolean | true:开启 100rel 协议 false:关闭 100rel 协议 |
| sipT38Support | O | Boolean | true:允许 t38 协议 false:禁止 t38 协议 |
| sipPrivacySupport | O | Boolean | true:识别 Privacy false:忽略 Privacy |
| sipPrivacy | O | Integer | 0:无 1:透传 2:id 3:none |
| sipPPreferredIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| sipPAssertedIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| dtmfReceiveMethod | O | Integer | DTMF 接收方式 0:所有 10:RFC2833 20:信令方式 30:关闭 |
| dtmfSIPSendMethod | O | Integer | SIP DTMF 发送方式 0:自动 10:RFC2833 50:SIP INFO 60:关闭 |
| sipCodecAssign | O | Boolean | true:指定 SIP  媒体编码 false:自动协商 SIP 媒体编码 |
| sipCodecs | O | String [] | 媒体编码范围 audio/AMR audio/DVI4 audio/G722 audio/G723 audio/G726-16 audio/G726-24 audio/G726-32 audio/G726-40 audio/G728 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
|  |  |  | audio/G729 audio/G729D audio/G729E audio/GSM audio/GSM-EFR audio/iLBC audio/L8 audio/L16   audio/LPC  audio/MPA audio/parityfec audio/PCMA audio/PCMU audio/QCELP audio/RED audio/VDVI audio/Speex audio/Speex-FEC audio/Speex-Wideband audio/Speex-Wideband-FEC audio/SILK   video/BT656 video/CelB  video/JPEG video/H261 video/H263 video/H263-1998 video/H263-2000 video/H264 video/MPV  video/MP2T video/MP1S video/MP2P video/parityfec video/RED video/BMPEG video/nv video/VP8 |
| audioCodecTranscodingEn able | O | Boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | O | Boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
|  |  |  | (inband)DTMF |
| rtpNeedDtmfInband | O | Boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| ivrEquipmentType | O | Integer | 语音设备类型 -1:无 1:直拨回拨 2:企业总机 3:增值业务 |
| ivrServiceName | O | String | 语音业务名称 |
| ivrCallbackBillingMode | O | Integer | 回拨计费 0:接入号对应话机 1:在用电话卡 2:自适应（顺序:绑定号码－在用电 话卡－主叫号对应话机－接入号对 应话机） 3:主叫号对应话机 |
| ivrCallbackMergeBillingM ode | O | Integer | 回拨第二路叠加计费方式 0:无 1:叠加接入号到第二路 2:叠加主叫号码到第二路 |
| ivrDirectMergeBillingMod e | O | Integer | 直拨第二路叠加计费方式 0:无 1:叠加接入号到第二路 2:叠加主叫号码到第二路 |
| ivrSecondBillingMode | O | Integer | 第二路计费方式 0:接入号对应话机 1:在用电话卡 3:主叫号对应话机 |
| ivrCallbackBillingSecordN otConnectedOnAccessE16  4 | O | Boolean | true:第二路未接通则按照接入号对 应话机计费 false:此参数不生效 |
| ivrCallbackBillingSecordC onnectedOnSecondAccoun t | O | Boolean | true:第二路接通则按照第二路账户 计费 false:此参数不生效 |
| ivrAccessVerifyActivePho neCard | O | Boolean | true:主叫号码校验在用电话卡 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ivrAccessVerifyBindedE16 4 | O | Boolean | true:主叫号码校验绑定号码 |
| ivrAccessVerifyCallerE164 Phone | O | Boolean | true:主叫号码校验平台话机 |
| ivrAccessVerifyAccessE16 4Phone | O | Boolean | true:被叫号码校验接入号存在账户 |
| ivrEnablePhoneSetting | O | Boolean | true:启用话机设设置 false:不启用话机设置 |
| lrnEnable | O | Boolean | LRN 查询 true:启用 false:禁用 |
| lrnEatPrefixLength | O | Integer | LRN 查询时忽略被叫号码前缀的长 度 |
| lrnFailureAction | O | Integer | 查询失败后的行为 0:拒绝此次呼叫 1:使用原有号码继续后续处理 |
| lrnInterstateBillingPrefix | O | String | LRN 查询后非同地区计费前缀 |
| lrnUndeterminedBillingPre fix | O | String | LRN 查询后有一个或两个号码无法 获知其地区时的计费前缀 |
| rewriteCalleeMobileAreaE nable | O | Boolean | true:开启手机区号添加 false:关闭手机区号添加 |
| rewriteCalleeMobileArea | O | String | 开启或关闭手机区号添加的地区信 息，采用逗号分隔多个地区 |
| callStateReport | O | Boolean | 开启或关闭呼叫状态通知 |
| sipRequestAddress | O | Integer | 0:Socket 1:Contact Port 2:Contact |
| sipResponseAddress | O | Integer | 0:Socket 1:Via Port 2:Via |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| password | O | String | 当创建请求未设置密码时，系统自 动生成随机密码 |

3.7 修改话机
接口地址/external/server/ModifyPhone
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 创建话机时同时创建计费账户 |
| password | O | String | 话机密码 |
| displayNumber | O | String | 去电显示 |
| lockType | O | Integer | 锁定类型 0:无锁定 1:锁定呼出 2:锁定呼入 3:全部锁定 |
| callLevel | O | Integer | 权限类型 1:网内通话 2:本地市话 3:国内长途 4:国际长途 |
| feerateGroup | O | String | 话机私有计费费率（请参考操作手 册费率相关描述）通常情况不使用 此设置 |
| monthlyMoneyMinimum | O | Double | 月最低消费额 |
| monthlyMoneyMaximum | O | Double | 月最高消费额 |
| monthlyRentFee | O | Double | 月租 |
| rewriteRulesOutCallee | O | LongString | 呼出被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCallee | O | LongString | 呼入被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCaller | O | LongString | 呼入主叫拨号规则，需符合拨号规 则书写格式 |
| routingGatewayGroupsAll ow | O | Boolean | true:仅允许设定的网关群组作为落 地 false:禁止设定的网关群组作为落地 |
| routingGatewayGroups | O | String | 落地网关群组名称（空表示所有） |
| account | O | String | 话机所属账户 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| equipment | O | String | 话机所属软交换（空表示属于所有 软交换） |
| calleeBilling | O | Boolean | true:开启被叫计费 false:普通计费（主叫计费） |
| customerPassword | O | String | Web 查询密码 |
| lineCallIn | O | Integer | 呼入线路数量限制 |
| lineCallOut | O | Integer | 呼出数量限制 |
| lineCapacity | O | Integer | 同时呼叫数限制（含呼入与呼出） |
| phonebookLimit | O | Integer | 电话簿数量限制 |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许主叫号码组呼入 false:禁止主叫号码组呼入 |
| callerLimitE164Groups | O | String | 当话机为被叫时 允许/禁止的主叫 号码组（空表示所有） |
| calleeLimitE164Allow | O | Boolean | true:允许呼出的被叫号码组 false:禁止呼出的被叫号码组 |
| calleeLimitE164Groups | O | String | 当话机为主叫时 允许/禁止的被叫 号码组（空表示所有） |
| dids | O | String | 一机多号 |
| memo | O | String | 备注 |
| infoPhoneValueAdded | O | InfoPhoneValueAdded | 话机增值业务 |
| infoPhoneAdditional | O | InfoPhoneAdditional | 话机补充设置 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.8 删除话机
接口地址/external/server/DeletePhone
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 电话号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.9 查询话机
接口地址/external/server/GetPhone
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164s | O | String [] | 电话号码列表(若 accounts 不设置则 此参数必选) |
| accounts | O | String [] | 账户号码列表(若e164s 不设置则此 参数必选) |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPhones | O | InfoPhone [] | 话机信息 |

InfoPhone 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 创建话机时同时创建计费账户 |
| password | O | String | 话机密码 |
| displayNumber | O | String | 去电显示 |
| lockType | O | Integer | 锁定类型 0:无锁定 1:锁定呼出 2:锁定呼入 3:全部锁定 |
| callLevel | O | Integer | 权限类型 1:网内通话 2:本地市话 3:国内长途 4:国际长途 |
| feerateGroup | O | String | 话机私有计费费率（请参考操作手 册费率相关描述）通常情况不使用 此设置 |
| monthlyMoneyMinimum | O | Double | 月最低消费额 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| monthlyMoneyMaximum | O | Double | 月最高消费额 |
| monthlyRentFee | O | Double | 月租 |
| rewriteRulesOutCallee | O | LongString | 呼出被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCallee | O | LongString | 呼入被叫拨号规则，需符合拨号规 则书写格式 |
| rewriteRulesInCaller | O | LongString | 呼入主叫拨号规则，需符合拨号规 则书写格式 |
| routingGatewayGroupsAll ow | O | Boolean | true:仅允许设定的网关群组作为落 地 false:禁止设定的网关群组作为落地 |
| routingGatewayGroups | O | String | 落地网关群组名称（空表示所有） |
| account | O | String | 话机所属账户 |
| equipment | O | String | 话机所属软交换 空:表示属于所有软交换 未选择:表示不属于任何软交换 |
| calleeBilling | O | Boolean | true:开启被叫计费 false:普通计费（主叫计费） |
| customerPassword | O | String | Web 查询密码 |
| lineCallIn | O | Integer | 呼入线路数量限制 |
| lineCallOut | O | Integer | 呼出数量限制 |
| lineCapacity | O | Integer | 同时呼叫数限制（含呼入与呼出） |
| phonebookLimit | O | Integer | 电话簿数量限制 |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许主叫号码组呼入 false:禁止主叫号码组呼入 |
| callerLimitE164Groups | O | String | 当话机为被叫时 允许/禁止的主叫 号码组（空表示所有） |
| calleeLimitE164Allow | O | Boolean | true:允许呼出的被叫号码组 false:禁止呼出的被叫号码组 |
| calleeLimitE164Groups | O | String | 当话机为主叫时 允许/禁止的被叫 号码组（空表示所有） |
| dids | O | String | 一机多号 |
| memo | O | String | 备注 |
| infoPhoneValueAdded | O | InfoPhoneValueAdded | 话机增值业务 |
| infoPhoneAdditional | O | InfoPhoneAdditional | 话机补充设置 |

3.10 查询在线话机
接口地址/external/server/GetPhoneOnline
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164s | M | String [] | 电话号码列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPhoneOnlines | O | InfoPhoneOnline [] | 在线话机信息 |

InfoPhoneOnline 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 电话号码 |
| currentCall | M | int | 当前呼叫总数 |
| remoteIp | M | String | 远端地址 |
| localIp | M | String | 本地地址 |
| registerTime | M | long | 注册时间（UTC 1970-01-01 至今的 毫秒数） |
| updateTime | M | long | 上次更新时间（UTC 1970-01-01 至 今的毫秒数） |
| protocol | M | int | 协议类型 0:H323 1:SIP |
| cryptoType | M | int | 加密类型 0:未加密 1:RC4 |
| productId | M | String | 设备名称 |

3.11 创建对接网关
接口地址/external/server/CreateGatewayMapping
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 对接网关名称 |
| password | O | String | 对接网关注册密码 |
| lockType | O | Integer | 锁定类型 0:无锁定 3:全部锁定 |
| callLevel | O | Integer | 权限类型 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |
| capacity | O | Integer | 线路上限 |
| priority | O | Integer | 优先级 |
| gatewayGroups | O | LongString | 所属网关群组（逗号分隔多个群组 名称） |
| routingGatewayGroupsAll ow | O | Boolean | true:允许使用落地群组 false:禁止使用落地群组 |
| routingGatewayGroups | O | LongString | 限制的落地网关群组名称，空串表 示所有 |
| registerType | O | Integer | 注册类型 0:静态 1:动态 3:IMS 边缘设备 |
| remoteIps | O | LongString | 对接网关 IP 地址列表（逗号分隔多 个 IP 地址） |
| callerE164CheckEnable | O | Boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | O | Boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | O | Boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164CheckOther | O | Boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |
| calleeE164CheckEnable | O | Boolean | true:检查被叫号码规范性 false:不检查被叫号码规范性 |
| calleeE164CheckCity | O | Boolean | true:允许被叫号码为城市号码 false:不允许被叫号码为城市号码 |
| calleeE164CheckMobile | O | Boolean | true:允许被叫号码为移动号码 false:不允许被叫号码为移动号码 |
| calleeE164CheckOther | O | Boolean | true:允许被叫号码为非城市号码与 非移动号码 false:不允许被叫号码为非城市号码 与非移动号码 |
| customerPassword | O | String | WEB 查询密码 |
| rtpForwardType | O | Integer | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |
| mediaCheckDirection | O | Integer | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| calleeE164Restrict | O | Integer | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| maxCallDurationLower | O | Integer | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | O | Integer | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |
| allowPhoneBilling | O | Boolean | 当主叫号码与平台话机号码匹配， 可使用话机号码的账户对呼叫进行 计费 |
| allowBindedE164Billing | O | Boolean | 当主叫号码与绑定号码匹配，可使 用绑定号码的账户对呼叫进行计费 |
| enablePhoneSetting | O | Boolean | 当主叫号码与平台话机号码匹配， 则主叫使用平台话机的配置进行后 续处理 |
| denySameCityCodesAllow | O | Boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | O | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |
| checkMobileAreaAllow | O | Boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | O | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| calloutCalleePrefixesAllow | O | Boolean | true:允许 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 false:禁止 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 |
| calloutCalleePrefixes | O | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |
| calloutCallerPrefixesAllow | O | Boolean | true:允许 calloutCallerPrefixes  设置 的前缀列表作为主叫号码前缀 false:禁止 calloutCallerPrefixes 设置 的前缀列表作为主叫号码前缀 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calloutCallerPrefixes | O | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| rewriteRulesOutCallee | O | LongString | 被叫拨号规则 |
| rewriteRulesOutCaller | O | LongString | 主叫拨号规则 |
| rewriteRulesInMobileArea Allow | O | Boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | O | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |
| timeoutCallProceeding | O | Integer | 呼叫未振铃或接通允许的最长持续 时长（单位:秒） -1:使用系统参数设置值 0:无限制 |
| sipResponseAddressMetho d | O | Integer | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |
| sipRequestAddressMethod | O | Integer | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |
| dtmfSendMethodH323 | O | Integer | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| dtmfSendMethodSIP | O | Integer | SIP 协议:软交换发送主叫DTMF 方 式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |
| dtmfReceiveMethod | O | Integer | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | O | Integer | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | O | Integer | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | O | Integer | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |
| q931ProgressIndicator | O | Integer | H323 协议中 Q931ProgressIndicator 的填写方式 -1:自动 0:关闭 1:ProgressNotEndToEndISDN 2:ProgressDestinationNonISDN 3:ProgressOriginNotISDN 4:ProgressReturnedToISDN 5:ProgressServiceChange 8:ProgressInbandInformationAvailabl e |
| account | O | String | 对接网关的计费账户号码 |
| callFailedQ931CauseValue | O | String | 将失败的终止原因转换为设定的 H323 终止原因，格式为<原始终止 原因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callFailedSipCode | O | String | 将失败的终止原因转换为设定的 SIP 终止原因，格式为<原始终止原 因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |
| sipRemoteRingSignal | O | Integer | SIP 远端回铃信令 0:自动 1:183+SDP 2:180+SDP |
| sipCalleeE164Domain | O | Integer | SIP 被叫号码取得方式 0:从信令头部 To 中取得 1:从信令头部 Invite 中取得 2:从信令头部 Diversion 中取得 |
| sipCallerE164Domain | O | Integer | SIP 主叫号码取得方式 0:从信令头部 From 中取得 1:从信令头部 RemotePartId 中取得 2:从信令头部 Display 中取得 3:从信令头部 P-Asserted-Identity 中 取得 4:从信令头部 P-Preferred-Identity 中 取得 |
| h323CalleeE164Domain | O | Integer | H323 被叫号码取得方式 0:从信令 CalledPartyNumber 中取得 1:从信令 DestinationAddress 中取得 |
| h323CallerE164Domain | O | Integer | H323 主叫号码取得方式 0:从信令 CallingPartyNumber  中取 得 1:从信令 SourceAddress 中取得 2:从信令 Display 中取得 |
| memo | O | String | 备注信息 |
| sipAuthenticationMethod | O | Integer | SIP 呼叫认证方式 0:根据 IP 地址认证 1:根据 IP 地址与端口共同认证 |
| h323FastStart | O | Boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| h323H245Tunneling | O | Boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |
| h323H245InSetup | O | Boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |
| h323AutoCallProceeding | O | Boolean | true:H323 协议收到呼叫请求后立即 回应 CallProceeding false:H323  协议收到呼叫后不立即 回应 CallProceeding |
| h323CallProceedingFromS IPTrying | O | Boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 Trying 信令对应的主 叫信令处理方式 true:转换为 CallProceeding  回应主 叫 false:不进行信令转换 |
| h323AlertingFromSIP183S dp | O | Boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 183+SDP  回应时对应 的主叫处理方式 true:转换为 Alerting 回应主叫 false:转换为 CallProceeding  回应主 叫 |
| h323T38 | O | Boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | O | Boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |
| sip100Rel | O | Boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | O | Boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipPrivacySupport | O | Boolean | true:识别 Privacy false:忽略 Privacy |
| groupE164Change | O | Boolean | true:启用号码变换功能 false:关闭号码变换功能 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerAllowLength | O | Integer | 主叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| calleeAllowLength | O | Integer | 被叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | O | String | 主叫号码组列表（可使用逗号分隔） |
| calleeLimitE164GroupsAll ow | O | Boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | O | String | 被叫号码组列表（可使用逗号分隔） |
| minProfitPercentEnable | O | Boolean | 是否开启最低利润率限制 |
| minProfitPercent | O | Integer | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | O | Boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | O | Double | 最高秒费率值（若分钟费率为 0.6， 此值应该设置为 0.01） |
| firstRoutePolicy | O | Integer | 第一路由策略: 0:无 1:接通率 2:最小秒费率 |
| secondRoutePolicy | O | Integer | 第二路由策略: 0:无 1:接通率 2:最小秒费率 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| h323G729SendMode | O | Integer | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729SendMode | O | Integer | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | O | Integer | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| sipG723Annexa | O | Integer | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | O | Boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | O | Vector<String> | H323 音频/视频列表 |
| sipCodecAssign | O | Boolean | true: 限制 SIP  音频/ 视频编码 为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | O | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | O | Boolean | true:允许使用编码转换 false:不允许使用编码转换 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| rtpIncludeDtmfInband | O | Boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | O | Boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| forwardSignalRewriteE164 GroupEnable | O | Boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |
| forwardSignalRewriteE164 Group | O | String | 呼叫前转信令改使用的号码群组名 称 |
| softswitchName | O | String | 软交换名称 |
| lrnEnable | O | Boolean | LRN 查询 true:启用 false:禁用 |
| lrnEatPrefixLength | O | Integer | LRN 查询时忽略被叫号码前缀的长 度 |
| lrnFailureAction | O | Integer | 查询失败后的行为 0:拒绝此次呼叫 1:使用原有号码继续后续处理 |
| lrnInterstateBillingPrefix | O | String | LRN 查询后非同地区计费前缀 |
| lrnUndeterminedBillingPre fix | O | String | LRN 查询后有一个或两个号码无法 获知其地区时的计费前缀 |
| language | O | String | 无法接通提示所使用的语言 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |
| proportionCalleePrefixs | O | ProportionCalleePrefix[] | 按比例被叫添加路由前缀 |

ProportionCalleePrefix 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| proportion | M | int | 比例值 |
| addPrefix | M | String | 添加前缀 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.12 修改对接网关
接口地址/external/server/ModifyGatewayMapping
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 对接网关名称 |
| password | O | String | 对接网关注册密码 |
| lockType | O | Integer | 锁定类型 0:无锁定 3:全部锁定 |
| callLevel | O | Integer | 权限类型 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |
| capacity | O | Integer | 线路上限 |
| priority | O | Integer | 优先级 |
| gatewayGroups | O | LongString | 所属网关群组（逗号分隔多个群组 名称） |
| routingGatewayGroupsAll ow | O | Boolean | true:允许使用落地群组 false:禁止使用落地群组 |
| routingGatewayGroups | O | LongString | 限制的落地网关群组名称，空串表 示所有 |
| registerType | O | Integer | 注册类型 0:静态 1:动态 3:IMS 边缘设备 |
| remoteIps | O | LongString | 对接网关 IP 地址列表（逗号分隔多 个 IP 地址） |
| callerE164CheckEnable | O | Boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | O | Boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | O | Boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164CheckOther | O | Boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |
| calleeE164CheckEnable | O | Boolean | true:检查被叫号码规范性 false:不检查主叫号码规范性 |
| calleeE164CheckCity | O | Boolean | true:允许被叫号码为城市号码 false:不允许被叫号码为城市号码 |
| calleeE164CheckMobile | O | Boolean | true:允许被叫号码为移动号码 false:不允许被叫号码为移动号码 |
| calleeE164CheckOther | O | Boolean | true:允许被叫号码为非城市号码与 非移动号码 false:不允许被叫号码为非城市号码 与非移动号码 |
| customerPassword | O | String | WEB 查询密码 |
| rtpForwardType | O | Integer | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |
| mediaCheckDirection | O | Integer | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| calleeE164Restrict | O | Integer | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| maxCallDurationLower | O | Integer | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | O | Integer | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |
| allowPhoneBilling | O | Boolean | 当主叫号码与平台话机号码匹配， 可使用话机号码的账户对呼叫进行 计费 |
| allowBindedE164Billing | O | Boolean | 当主叫号码与绑定号码匹配，可使 用绑定号码的账户对呼叫进行计费 |
| enablePhoneSetting | O | Boolean | 当主叫号码与平台话机号码匹配， 则主叫使用平台话机的配置进行后 续处理 |
| denySameCityCodesAllow | O | Boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | O | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |
| checkMobileAreaAllow | O | Boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | O | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| calloutCalleePrefixesAllow | O | Boolean | true:允许 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 false:禁止 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 |
| calloutCalleePrefixes | O | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |
| calloutCallerPrefixesAllow | O | Boolean | true:允许 calloutCallerPrefixes  设置 的前缀列表作为主叫号码前缀 false:禁止 calloutCallerPrefixes 设置 的前缀列表作为主叫号码前缀 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calloutCallerPrefixes | O | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| rewriteRulesOutCallee | O | LongString | 被叫拨号规则 |
| rewriteRulesOutCaller | O | LongString | 主叫拨号规则 |
| rewriteRulesInMobileArea Allow | O | Boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | O | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |
| timeoutCallProceeding | O | Integer | 呼叫未振铃或接通允许的最长持续 时长（单位:秒） -1:使用系统参数设置值 0:无限制 |
| sipResponseAddressMetho d | O | Integer | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |
| sipRequestAddressMethod | O | Integer | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |
| dtmfSendMethodH323 | O | Integer | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |
| dtmfSendMethodSIP | O | Integer | SIP 协议，软交换发送 DTMF 方式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| dtmfReceiveMethod | O | Integer | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | O | Integer | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | O | Integer | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | O | Integer | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |
| q931ProgressIndicator | O | Integer | H323 协议中 Q931ProgressIndicator 的填写方式 -1:自动 0:关闭 1:ProgressNotEndToEndISDN 2:ProgressDestinationNonISDN 3:ProgressOriginNotISDN 4:ProgressReturnedToISDN 5:ProgressServiceChange 8:ProgressInbandInformationAvailabl e |
| account | O | String | 对接网关的计费账户号码 |
| callFailedQ931CauseValue | O | String | 将失败的终止原因转换为设定的 H323 终止原因，格式为<原始终止 原因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |
| callFailedSipCode | O | String | 将失败的终止原因转换为设定的 SIP 终止原因，格式为<原始终止原 因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipRemoteRingSignal | O | Integer | SIP 远端回铃信令 0:自动 1:183+SDP 2:180+SDP |
| sipCalleeE164Domain | O | Integer | SIP 被叫号码取得方式 0:从信令头部 To 中取得 1:从信令头部 Invite 中取得 2:从信令头部 Diversion 中取得 |
| sipCallerE164Domain | O | Integer | SIP 主叫号码取得方式 0:从信令头部 From 中取得 1:从信令头部 RemotePartId 中取得 2:从信令头部 Display 中取得 3:从信令头部 P-Asserted-Identity 中 取得 4:从信令头部 P-Preferred-Identity 中 取得 |
| h323CalleeE164Domain | O | Integer | H323 被叫号码取得方式 0:从信令 CalledPartyNumber 中取得 1:从信令 DestinationAddress 中取得 |
| h323CallerE164Domain | O | Integer | H323 主叫号码取得方式 0:从信令 CallingPartyNumber  中取 得 1:从信令 SourceAddress 中取得 2:从信令 Display 中取得 |
| memo | O | String | 备注信息 |
| sipAuthenticationMethod | O | Integer | SIP 呼叫认证方式 0:根据 IP 地址认证 1:根据 IP 地址与端口共同认证 |
| h323FastStart | O | Boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |
| h323H245Tunneling | O | Boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |
| h323H245InSetup | O | Boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| h323AutoCallProceeding | O | Boolean | true:H323 协议收到呼叫请求后立即 回应 CallProceeding false:H323  协议收到呼叫后不立即 回应 CallProceeding |
| h323CallProceedingFromS IPTrying | O | Boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 Trying 信令对应的主 叫信令处理方式 true:转换为 CallProceeding  回应主 叫 false:不进行信令转换 |
| h323AlertingFromSIP183S dp | O | Boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 183+SDP  回应时对应 的主叫处理方式 true:转换为 Alerting 回应主叫 false:转换为 CallProceeding  回应主 叫 |
| h323T38 | O | Boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | O | Boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |
| sip100Rel | O | Boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | O | Boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipPrivacySupport | O | Boolean | true:识别 Privacy false:忽略 Privacy |
| groupE164Change | O | Boolean | true:启用号码变换功能 false:关闭号码变换功能 |
| callerAllowLength | O | Integer | 主叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| calleeAllowLength | O | Integer | 被叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | O | String | 主叫号码组列表（可使用逗号分隔） |
| calleeLimitE164GroupsAll ow | O | Boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | O | String | 被叫号码组列表（可使用逗号分隔） |
| minProfitPercentEnable | O | Boolean | 是否开启最低利润率限制 |
| minProfitPercent | O | Integer | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | O | Boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | O | Double | 最高秒费率值（若分钟费率为 0.6， 此值应该设置为0.01） |
| firstRoutePolicy | O | Integer | 第一路由策略: 0:无 1:接通率 2:最小秒费率 |
| secondRoutePolicy | O | Integer | 第二路由策略: 0:无 1:接通率 2:最小秒费率 |
| h323G729SendMode | O | Integer | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipG729SendMode | O | Integer | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | O | Integer | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| sipG723Annexa | O | Integer | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | O | Boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | O | Vector<String> | H323 音频/视频列表 |
| sipCodecAssign | O | Boolean | true: 限制 SIP  音频/ 视频编码为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | O | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | O | Boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | O | Boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | O | Boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| forwardSignalRewriteE164 GroupEnable | O | Boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| forwardSignalRewriteE164 Group | O | String | 呼叫前转信令改使用的号码群组名 称 |
| lrnEnable | O | Boolean | LRN 查询 true:启用 false:禁用 |
| lrnEatPrefixLength | O | Integer | LRN 查询时忽略被叫号码前缀的长 度 |
| lrnFailureAction | O | Integer | 查询失败后的行为 0:拒绝此次呼叫 1:使用原有号码继续后续处理 |
| lrnInterstateBillingPrefix | O | String | LRN 查询后非同地区计费前缀 |
| lrnUndeterminedBillingPre fix | O | String | LRN 查询后有一个或两个号码无法 获知其地区时的计费前缀 |
| language | O | String | 无法接通提示所使用的语言 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |
| proportionCalleePrefixs | O | ProportionCalleePrefix[] | 按比例被叫添加路由前缀 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.13 查询对接网关
接口地址/external/server/GetGatewayMapping
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | M | String [] | 网关名称 不设置表示获取所有对接网关信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoGatewayMappings | O | InfoGatewayMapping [] | 话机信息 |

类型 InfoGatewayMapping 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 对接网关名称 |
| lockType | M | int | 锁定类型 0:无锁定 1:锁定呼出 2:锁定呼入 3:全部锁定 |
| callLevel | M | int | 权限类型 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |
| capacity | M | int | 线路上限 |
| priority | M | int | 优先级 |
| gatewayGroups | M | LongString | 所属网关群组（逗号分隔多个群组 名称） |
| routingGatewayGroupsAll ow | M | boolean | true:允许使用落地群组 false:禁止使用落地群组 |
| routingGatewayGroups | M | LongString | 限制的落地网关群组名称，空串表 示所有 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| registerType | M | int | 注册类型 0:静态 1:动态 3:IMS 边缘设备 |
| remoteIps | M | LongString | 对接网关 IP 地址列表（逗号分隔多 个 IP 地址） |
| callerE164CheckEnable | M | boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | M | boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | M | boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |
| callerE164CheckOther | M | boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |
| calleeE164CheckEnable | M | boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| calleeE164CheckCity | M | boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| calleeE164CheckMobile | M | boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |
| calleeE164CheckOther | M | boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |
| rtpForwardType | M | int | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| mediaCheckDirection | M | int | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| calleeE164Restrict | M | int | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |
| maxCallDurationLower | M | int | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | M | int | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |
| allowPhoneBilling | M | boolean | 当主叫号码与平台话机号码匹配， 可使用话机号码的账户对呼叫进行 计费 |
| allowBindedE164Billing | M | boolean | 当主叫号码与绑定号码匹配，可使 用绑定号码的账户对呼叫进行计费 |
| enablePhoneSetting | M | boolean | 当主叫号码与平台话机号码匹配， 则主叫使用平台话机的配置进行后 续处理 |
| denySameCityCodesAllow | M | boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | M | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| checkMobileAreaAllow | M | boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | M | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| calloutCalleePrefixesAllow | M | boolean | true:允许 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 false:禁止 calloutCalleePrefixes 设置 的前缀列表作为被叫号码前缀 |
| calloutCalleePrefixes | M | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |
| calloutCallerPrefixesAllow | M | boolean | true:允许 calloutCallerPrefixes  设置 的前缀列表作为主叫号码前缀 false:禁止 calloutCallerPrefixes 设置 的前缀列表作为主叫号码前缀 |
| calloutCallerPrefixes | M | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| rewriteRulesOutCallee | M | LongString | 被叫拨号规则 |
| rewriteRulesOutCaller | M | LongString | 主叫拨号规则 |
| rewriteRulesInMobileArea Allow | M | boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | M | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |
| timeoutCallProceeding | M | int | 呼叫未振铃或接通允许的最长持续 时长（单位:秒） -1:使用系统参数设置值 0:无限制 |
| sipResponseAddressMetho d | M | int | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipRequestAddressMethod | M | int | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |
| dtmfSendMethodH323 | M | int | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |
| dtmfSendMethodSIP | M | int | SIP 协议，软交换发送 DTMF 方式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |
| dtmfReceiveMethod | M | int | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | M | int | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | M | int | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | M | int | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| q931ProgressIndicator | M | int | H323 协议中 Q931ProgressIndicator 的填写方式 -1:自动 0:关闭 1:ProgressNotEndToEndISDN 2:ProgressDestinationNonISDN 3:ProgressOriginNotISDN 4:ProgressReturnedToISDN 5:ProgressServiceChange 8:ProgressInbandInformationAvailabl e |
| account | M | String | 对接网关的计费账户号码 |
| accountName | M | String | 对接网关的计费账户名称 |
| password | M | String | 对接网关注册密码 |
| customerPassword | M | String | 对接网关 web 查询密码 |
| callFailedQ931CauseValue | M | String | 将失败的终止原因转换为设定的 H323 终止原因，格式为<原始终止 原因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |
| callFailedSipCode | M | String | 将失败的终止原因转换为设定的 SIP 终止原因，格式为<原始终止原 因>:<目标终止原因> 原始终止原因 0:其它 目标终止原因 0:不替换 大于0:请参考H323/SIP 协议通话中 断定义规范 |
| sipRemoteRingSignal | M | int | SIP 远端回铃信令 0:自动 1:183+SDP 2:180+SDP |
| sipCalleeE164Domain | M | int | SIP 被叫号码取得方式 0:从信令头部 To 中取得 1:从信令头部 Invite 中取得 2:从信令头部 Diversion 中取得 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipCallerE164Domain | M | int | SIP 主叫号码取得方式 0:从信令头部 From 中取得 1:从信令头部 RemotePartId 中取得 2:从信令头部 Display 中取得 3:从信令头部 P-Asserted-Identity 中 取得 4:从信令头部 P-Preferred-Identity 中 取得 |
| h323CalleeE164Domain | M | int | H323 被叫号码取得方式 0:从信令 CalledPartyNumber 中取得 1:从信令 DestinationAddress 中取得 |
| h323CallerE164Domain | M | int | H323 主叫号码取得方式 0:从信令 CallingPartyNumber  中取 得 1:从信令 SourceAddress 中取得 2:从信令 Display 中取得 |
| memo | M | String | 备注信息 |
| sipAuthenticationMethod | M | int | SIP 呼叫认证方式 0:根据 IP 地址认证 1:根据 IP 地址与端口共同认证 |
| h323FastStart | M | boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |
| h323H245Tunneling | M | boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |
| h323H245InSetup | M | boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |
| h323AutoCallProceeding | M | boolean | true:H323 协议收到呼叫请求后立即 回应 CallProceeding false:H323  协议收到呼叫后不立即 回应 CallProceeding |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| h323CallProceedingFromS IPTrying | M | boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 Trying 信令对应的主 叫信令处理方式 true:转换为 CallProceeding  回应主 叫 false:不进行信令转换 |
| h323AlertingFromSIP183S dp | M | boolean | 主叫为 H323 协议被叫为 SIP 协议 时，被叫接收 183+SDP  回应时对应 的主叫处理方式 true:转换为 Alerting 回应主叫 false:转换为 CallProceeding  回应主 叫 |
| h323T38 | M | boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | M | boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |
| sip100Rel | M | boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | M | boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipPrivacySupport | O | Boolean | true:识别 Privacy false:忽略 Privacy |
| groupE164Change | M | boolean | true:启用号码变换功能 false:关闭号码变换功能 |
| callerAllowLength | M | int | 主叫号码允许的号码长度 |
| calleeAllowLength | M | int | 被叫号码允许的号码长度 |
| callerLimitE164GroupsAll ow | M | boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | M | String | 主叫号码组列表（可使用逗号分隔） |
| calleeLimitE164GroupsAll ow | M | boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | M | String | 被叫号码组列表（可使用逗号分隔） |
| minProfitPercentEnable | M | boolean | 是否开启最低利润率限制 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| minProfitPercent | M | int | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | M | boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | M | double | 最高秒费率值 |
| firstRoutePolicy | M | int | 第一路由策略: 0:无 1:接通率 2:最小秒费率 |
| secondRoutePolicy | M | int | 第二路由策略: 0:无 1:接通率 2:最小秒费率 |
| h323G729SendMode | M | int | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729SendMode | M | int | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | M | int | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipG723Annexa | M | int | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | M | boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | M | Vector<String> | H323 音频/视频列表 |
| sipCodecAssign | M | boolean | true: 限制 SIP  音频/ 视频编码为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | M | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | M | boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | M | boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | M | boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| softswitchName | M | String | 软交换名称 未设置:表示不属于任何软交换 空串:表示属于所有软交换 |
| forwardSignalRewriteE164 GroupEnable | M | boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |
| forwardSignalRewriteE164 Group | M | String | 呼叫前转信令改使用的号码群组名 称 |
| lrnEnable | M | boolean | LRN 查询 true:启用 false:禁用 |
| lrnEatPrefixLength | M | int | LRN 查询时忽略被叫号码前缀的长 度 |
| lrnFailureAction | M | int | 查询失败后的行为 0:拒绝此次呼叫 1:使用原有号码继续后续处理 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| lrnInterstateBillingPrefix | M | String | LRN 查询后非同地区计费前缀 |
| lrnUndeterminedBillingPre fix | M | String | LRN 查询后有一个或两个号码无法 获知其地区时的计费前缀 |
| language | M | String | 无法接通提示所使用的语言 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |
| proportionCalleePrefixs | O | ProportionCalleePrefix[] | 按比例被叫添加路由前缀 |

3.14 删除对接网关
接口地址/external/server/DeleteGatewayMapping
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 对接网关名称 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.15 查询在线对接网关
接口地址/external/server/GetGatewayMappingOnline
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | O | String [] | 对接网关名称 不设置:表示此过滤条件无效 |
| softswitchName | O | String | 软交换名称 不设置:表示此过滤条件无效，查询 所有的软交换 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoGatewayMappingOnlin es | O | InfoGatewayMappingOnli ne [] | 套餐订单列表 |

类型 InfoGatewayMappingOnline 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 对接网关 ID |
| name | M | String | 对接网关名称 |
| currentCall | M | int | 当前呼叫总数 |
| capacity | M | int | 呼叫线路上限 |
| asr | M | double | 呼叫应答率 |
| acd | M | long | 平均通话时长（单位:秒） |
| remoteIps | M | String | 远端地址（逗号分隔多个 IP） |
| natIp | O | String | NAT 内部地址，仅在网关与软交换 间存在地址转换设备时有效 |
| localIp | M | String | 注册本地地址 |
| registerTime | M | long | 注册时间（UTC 1970-01-01 至今的 毫秒数） 0:静态网关 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| updateTime | M | long | 上次更新时间（UTC 1970-01-01 至 今的毫秒数） 0:静态网关 |
| keepTime | M | long | 在线时间（单位:秒） 0:静态网关 |
| cryptoType | M | int | 加密类型 0:未加密 1:RC4 |
| softswitchName | M | String | 软交换名称 |
| softswitchIp | M | String | 软交换 IP |

3.16 创建落地网关
接口地址/external/server/CreateGatewayRouting
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 落地网关名称 |
| prefix | O | String | 落地网关前缀（可使用逗号分隔） |
| prefixStyle | O | Integer | 前缀匹配方式 0:终结模式 1:延续模式 |
| password | O | String | 落地网关注册密码 |
| customerPassword | O | String | 落地网关 web 查询密码 |
| gatewayGroups | O | String | 所属网关群组（逗号分隔多个群组 名称） |
| capacity | O | Integer | 线路上限 |
| lockType | O | Integer | 锁定类型 0:无锁定 3:全部锁定 |
| priority | O | Integer | 优先级 |
| registerType | O | Integer | 注册类型 0:静态 1:动态 2:注册（向其他平台进行注册） 3:IMS 边缘设备 |
| remoteIp | O | String | 落地网关远端地址 |
| rtpForwardType | O | Integer | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |
| encrypt | O | Boolean | true:加密 false:不加密 |
| protocol | O | Integer | 信令协议 0:H323 1:SIP |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| signalPort | O | Integer | 信令端口 |
| localIp | O | String | 本地地址 空:表示由系统自行选择本地地址 |
| mediaCheckDirection | O | Integer | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| maxCallDurationLower | O | Integer | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | O | Integer | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |
| calleeE164Restrict | O | Integer | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |
| callerE164CheckEnable | O | Boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | O | Boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | O | Boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |
| callerE164CheckOther | O | Boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeE164CheckEnable | O | Boolean | true:检查被叫号码规范性 false:不检查被叫号码规范性 |
| calleeE164CheckCity | O | Boolean | true:允许被号码为城市号码 false:不允许被叫号码为城市号码 |
| calleeE164CheckMobile | O | Boolean | true:允许被叫号码为移动号码 false:不允许被叫号码为移动号码 |
| calleeE164CheckOther | O | Boolean | true:允许被叫号码为非城市号码与 非移动号码 false:不允被主叫号码为非城市号码 与非移动号码 |
| callinCallerPrefixesAllow | O | Boolean | true:允许 callinCallerPrefixes 设置的 前缀列表作为主叫号码前缀 false:禁止 callinCallerPrefixes  设置 的前缀列表作为主叫号码前缀 |
| callinCallerPrefixes | O | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| callinCalleePrefixesAllow | O | Boolean | true:允许callinCalleePrefixes 设置的 前缀列表作为被叫号码前缀 false:禁止 callinCalleePrefixes  设置 的前缀列表作为被叫号码前缀 |
| callinCalleePrefixes | O | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |
| callinForwardPrefixesAllo w | O | Boolean | true:允许 callinForwardPrefixes 设置 的前缀列表作为前转号码前缀 false:禁止 callinForwardPrefixes  设 置的前缀列表作为前转号码前缀 |
| callinForwardPrefixes | O | LongString | 前转号码限制功能中前转号码前缀 列表（可使用逗号分隔） |
| rewriteRulesInCaller | O | LongString | 主叫拨号规则 |
| rewriteRulesInCallee | O | LongString | 被叫拨号规则 |
| rewriteRulesInMobileArea Allow | O | Boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | O | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| timeoutSetup | O | Integer | H323 Setup 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceeding | O | Integer | H323  CallProceeding 超时时间（单 位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceedingOlc | O | Integer | H323   CallProceeding   包 含 Open   Logical Channel 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutAlerting | O | Integer | H323 Alerting 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutInvite | O | Integer | SIP Invite 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutTrying | O | Integer | SIP Trying 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgressSd p | O | Integer | SIP  SessionProgress 含 SDP 超时时 间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgress | O | Integer | SIP SessionProgress 超时时间（单位: 秒） 0:表示使用系统参数设定值 |
| timeoutRinging | O | Integer | SIP Ring 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| denyCallerCalleeAllow | O | Boolean | true:允许 denyCallerCallee 设置的主 叫向对应被叫进行呼叫 false:禁止 denyCallerCallee  设置的 主向叫对应被叫进行呼叫 |
| denyCallerCallee | O | LongString | 主叫向对应被叫进行呼叫的限制列 表格 式 为 [< 主 叫 号码>:< 被 叫 号 码>[,<主叫号码>:<被叫号码>]…]    例如:025:010,021:023 |
| denySameCityCodesAllow | O | Boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | O | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| checkMobileAreaAllow | O | Boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | O | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| switchAllowRing | O | Boolean | 收到振铃信令 18x 后的网关切换方 式 false:禁止 true:允许 |
| switchAllowSdp | O | Boolean | SIP 协议时，当信令内包含 Sdp 时 的后续处理方式 false:禁止 true:允许 |
| switchAllowRtp | O | Boolean | 当在媒体转发时收到来自远端的媒 体报文时的后续处理方式 false:禁止 true:允许 |
| switchAllowBusy | O | Boolean | 当收到被叫忙后的后续处理方式 false:禁止 true:允许 |
| switchAllowErrorCode | O | Boolean | 收到列表内错误码，后续网关切换 方式 false:禁止 true:允许 |
| sipResponseAddressMetho d | O | Integer | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |
| sipRequestAddressMethod | O | Integer | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| dtmfSendMethodH323 | O | Integer | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |
| dtmfSendMethodSIP | O | Integer | SIP 协议，软交换发送 DTMF 方式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |
| dtmfReceiveMethod | O | Integer | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | O | Integer | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | O | Integer | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | O | Integer | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |
| q931NumberingPlan | O | Integer | Q931NumberingPlan -1:默认，使用系统参数设定 0:UnknownPlan 1:ISDNPlan 3:DataPlan 4:TelexPlan 8:NationalStandardPlan 9:PrivatePlan 15:ReservedPlan |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| q931NumberType | O | Integer | Q931NumberType -1:默认，使用系统参数设定 0:UnknownType 1:InternationalType 2:NationalType 3:NetworkSpecificType 4:SubscriberType 6:AbbreviatedType 7:ReservedType |
| q931PresentationIndicator | O | Integer | Q931PresentationIndicator -1:默认，使用系统参数设定 0:Presentation allowed 1:Presentation restricted 2:Number    not    available    due    to interworking 3:Reserved 4:无 |
| q931ScreeningIndicator | O | Integer | Q931ScreeningIndicator -1:默认，使用系统参数设定 0:User-provided ，not screened 1:User-provided ，verified and passed 2:User-provided ，verified and failed  3:Network provided 4:无 |
| clearingAccount | O | String | 结算账户名称 |
| h323FastStart | O | Boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |
| h323H245Tunneling | O | Boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |
| h323H245InSetup | O | Boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |
| h323T38 | O | Boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | O | Boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sip100Rel | O | Boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | O | Boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipDisplay | O | Boolean | true: 在 向 远 端 发 送 信 令 时 包 含 Display  头部 false:在向远端发送信 令时不包含 Display 头部 |
| sipRemotePartyId | O | Boolean | true: 在 向 远 端 发 送 信 令 时 包 含 RemotePartyId 头部 false:在向远端发送信令时不包含 RemotePartyId 头部 |
| sipPrivacy | O | Integer | 0:无 1:透传 2:id 3:none |
| sipPPreferredIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| sipPAssertedIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| groupE164Change | O | Boolean | true:启用号码变换功能 false:关闭号码变换功能 |
| callerAllowLength | O | Integer | 主叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| calleeAllowLength | O | Integer | 被叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | O | String | 主叫号码组列表（可使用逗号分隔） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeLimitE164GroupsAll ow | O | Boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | O | String | 被叫号码组列表（可使用逗号分隔） |
| h323G729SendMode | O | Integer | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729SendMode | O | Integer | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | O | Integer | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| sipG723Annexa | O | Integer | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | O | Boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | O | Vector<String> | H323 音频/视频列表 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipCodecAssign | O | Boolean | true: 限制 SIP  音频/ 视频编码为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | O | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | O | Boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | O | Boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | O | Boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| feerateRestrict | O | Boolean | true:校验被叫号码费率 false:不校验费率 |
| leastCostRouting | O | Boolean | 最低秒费率排序（在 feerateRestrict 为 true 时有效） true:启用 false:关闭 |
| minProfitPercentEnable | O | Boolean | feerateRestrict 为 true 时有效 是否开启最低利润率限制 |
| minProfitPercent | O | Integer | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | O | Boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | O | Double | 最高秒费率值（若分钟费率为 0.6， 此值应该设置为0.01） |
| enablePhoneDisplay | O | Boolean | true:主叫为话机时使用话机的去电 显示作为主叫号码 false:主叫为话机时使用话机的号码 显示作为主叫号码 |
| clearingAccountUseCallou tE164 | O | Boolean | true:使用拨号规则后的被叫号码作 为结算账户计费被叫 false:使用拨号规则前的被叫号码作 为结算账户计费被叫 |
| softswitchName | O | String | 软交换名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| forwardSignalRewriteE164 GroupEnable | O | Boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |
| forwardSignalRewriteE164 Group | O | String | 呼叫前转信令改使用的号码群组名 称 |
| memo | O | String | 备注 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| externalNumberVerifyBits | O | Long | 智能黑名单，该参数采用 bit  位控 制，每一位表示开启某项功能 1<<0:开启智能黑名单 1<<1:保险营销 1<<2:股票推荐 1<<3:房产新盘 1<<4:教育培训 1<<5:M0/M1 催收 1<<6:房产中介 1<<7:问卷调查 1<<8:车险回访 1<<9:客服通知 1<<10:金融营销   1<<11:语音验证码 |
| externalNumberVerifyRew riteCaller | O | String | 智能黑名单主叫拨号规则 |
| externalNumberVerifyRew riteCallee | O | String | 智能黑名单被叫拨号规则 |
| scheduledCallinPrefixes | O | InfoScheduledCallinPrefix es[] | 时段呼叫限制 |
| rewriteRulesInCallerUseE1 64GroupEnable | O | Boolean | 主叫号码池 false：关闭 true：启用 |
| rewriteRulesInCallerUseE1 64Group | O | String | 主叫号码池 号码组组名称 |
| rewriteRulesInCallerUseE1 64Line | O | Integer | 主叫号码池号码复用次数 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| signalPortLocal | O | Integer | 信令本地端口 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |

InfoScheduledCallinPrefixes 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| days | M | int [] | 星期几 0:星期日 1:星期一 2:星期二 3:星期三 4:星期四 5:星期五 6:星期六 |
| beginTime | M | int | 一日中的起始秒 取值范围(0~86400) |
| endTime | M | int | 一日中的终止秒 取值范围(0~86400) |
| action | M | int | 操作 0:禁止 1:允许 |
| type | M | int | 方式 0:主叫 1:被叫 |
| prefixes | M | String [] | 前缀列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.17 修改落地网关
接口地址/external/server/ModifyGatewayRouting
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 落地网关名称 |
| prefix | O | String | 落地网关前缀（可使用逗号分隔） |
| prefixStyle | O | Integer | 前缀匹配方式 0:终结模式 1:延续模式 |
| password | O | String | 落地网关注册密码 |
| customerPassword | O | String | 落地网关 web 查询密码 |
| gatewayGroups | O | String | 所属网关群组（逗号分隔多个群组 名称） |
| capacity | O | Integer | 线路上限 |
| lockType | O | Integer | 锁定类型 0:无锁定 3:全部锁定 |
| priority | O | Integer | 优先级 |
| registerType | O | Integer | 注册类型 0:静态 1:动态 2:注册（向其他平台进行注册） 3:IMS 边缘设备 |
| remoteIp | O | String | 落地网关远端地址 |
| rtpForwardType | O | Integer | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |
| encrypt | O | Boolean | true:加密 false:不加密 |
| protocol | O | Integer | 信令协议 0:H323 1:SIP |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| signalPort | O | Integer | 信令端口 |
| localIp | O | String | 本地地址 空:表示由系统自行选择本地地址 |
| mediaCheckDirection | O | Integer | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| maxCallDurationLower | O | Integer | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | O | Integer | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |
| calleeE164Restrict | O | Integer | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |
| callerE164CheckEnable | O | Boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | O | Boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | O | Boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |
| callerE164CheckOther | O | Boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeE164CheckEnable | O | Boolean | true:检查被叫号码规范性 false:不检查被叫号码规范性 |
| calleeE164CheckCity | O | Boolean | true:允许被号码为城市号码 false:不允许被叫号码为城市号码 |
| calleeE164CheckMobile | O | Boolean | true:允许被叫号码为移动号码 false:不允许被叫号码为移动号码 |
| calleeE164CheckOther | O | Boolean | true:允许被叫号码为非城市号码与 非移动号码 false:不允被主叫号码为非城市号码 与非移动号码 |
| callinCallerPrefixesAllow | O | Boolean | true:允许 callinCallerPrefixes 设置的 前缀列表作为主叫号码前缀 false:禁止 callinCallerPrefixes  设置 的前缀列表作为主叫号码前缀 |
| callinCallerPrefixes | O | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| callinCalleePrefixesAllow | O | Boolean | true:允许callinCalleePrefixes 设置的 前缀列表作为被叫号码前缀 false:禁止 callinCalleePrefixes  设置 的前缀列表作为被叫号码前缀 |
| callinCalleePrefixes | O | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |
| callinForwardPrefixesAllo w | O | Boolean | true:允许 callinForwardPrefixes 设置 的前缀列表作为前转号码前缀 false:禁止 callinForwardPrefixes  设 置的前缀列表作为前转号码前缀 |
| callinForwardPrefixes | O | LongString | 前转号码限制功能中前转号码前缀 列表（可使用逗号分隔） |
| rewriteRulesInCaller | O | LongString | 主叫拨号规则 |
| rewriteRulesInCallee | O | LongString | 被叫拨号规则 |
| rewriteRulesInMobileArea Allow | O | Boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | O | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| timeoutSetup | O | Integer | H323 Setup 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceeding | O | Integer | H323  CallProceeding 超时时间（单 位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceedingOlc | O | Integer | H323   CallProceeding   包 含 Open   Logical Channel 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutAlerting | O | Integer | H323 Alerting 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutInvite | O | Integer | SIP Invite 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutTrying | O | Integer | SIP Trying 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgressSd p | O | Integer | SIP  SessionProgress 含 SDP 超时时 间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgress | O | Integer | SIP SessionProgress 超时时间（单位: 秒） 0:表示使用系统参数设定值 |
| timeoutRinging | O | Integer | SIP Ring 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| denyCallerCalleeAllow | O | Boolean | true:允许 denyCallerCallee 设置的主 叫向对应被叫进行呼叫 false:禁止 denyCallerCallee  设置的 主向叫对应被叫进行呼叫 |
| denyCallerCallee | O | LongString | 主叫向对应被叫进行呼叫的限制列 表格 式 为 [< 主 叫 号码>:< 被 叫 号 码>[,<主叫号码>:<被叫号码>]…]    例如:025:010,021:023 |
| denySameCityCodesAllow | O | Boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | O | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| checkMobileAreaAllow | O | Boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | O | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| switchAllowRing | O | Boolean | 收到振铃信令 18x 后的网关切换方 式 false:禁止 true:允许 |
| switchAllowSdp | O | Boolean | SIP 协议时，当信令内包含 Sdp 时 的后续处理方式 false:禁止 true:允许 |
| switchAllowRtp | O | Boolean | 当在媒体转发时收到来自远端的媒 体报文时的后续处理方式 false:禁止 true:允许 |
| switchAllowBusy | O | Boolean | 当收到被叫忙后的后续处理方式 false:禁止 true:允许 |
| switchAllowErrorCode | O | Boolean | 收到列表内错误码，后续网关切换 方式 false:禁止 true:允许 |
| sipResponseAddressMetho d | O | Integer | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |
| sipRequestAddressMethod | O | Integer | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| dtmfSendMethodH323 | O | Integer | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |
| dtmfSendMethodSIP | O | Integer | SIP 协议，软交换发送 DTMF 方式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |
| dtmfReceiveMethod | O | Integer | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | O | Integer | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | O | Integer | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | O | Integer | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |
| q931NumberingPlan | O | Integer | Q931NumberingPlan -1:默认，使用系统参数设定 0:UnknownPlan 1:ISDNPlan 3:DataPlan 4:TelexPlan 8:NationalStandardPlan 9:PrivatePlan 15:ReservedPlan |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| q931NumberType | O | Integer | Q931NumberType -1:默认，使用系统参数设定 0:UnknownType 1:InternationalType 2:NationalType 3:NetworkSpecificType 4:SubscriberType 6:AbbreviatedType 7:ReservedType |
| q931PresentationIndicator | O | Integer | Q931PresentationIndicator -1:默认，使用系统参数设定 0:Presentation allowed 1:Presentation restricted 2:Number    not    available    due    to interworking 3:Reserved 4:无 |
| q931ScreeningIndicator | O | Integer | Q931ScreeningIndicator -1:默认，使用系统参数设定 0:User-provided ，not screened 1:User-provided ，verified and passed 2:User-provided ，verified and failed  3:Network provided 4:无 |
| clearingAccount | O | String | 结算账户名称 |
| h323FastStart | O | Boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |
| h323H245Tunneling | O | Boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |
| h323H245InSetup | O | Boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |
| h323T38 | O | Boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | O | Boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sip100Rel | O | Boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | O | Boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipDisplay | O | Boolean | true: 在 向 远 端 发 送 信 令 时 包 含 Display  头部 false:在向远端发送信 令时不包含 Display 头部 |
| sipRemotePartyId | O | Boolean | true: 在 向 远 端 发 送 信 令 时 包 含 RemotePartyId 头部 false:在向远端发送信令时不包含 RemotePartyId 头部 |
| sipPrivacy | O | Integer | 0:无 1:透传 2:id 3:none |
| sipPPreferredIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| sipPAssertedIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| groupE164Change | O | Boolean | true:启用号码变换功能 false:关闭号码变换功能 |
| callerAllowLength | O | Integer | 主叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| calleeAllowLength | O | Integer | 被叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| callerLimitE164GroupsAll ow | O | Boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | O | String | 主叫号码组列表（可使用逗号分隔） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeLimitE164GroupsAll ow | O | Boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | O | String | 被叫号码组列表（可使用逗号分隔） |
| h323G729SendMode | O | Integer | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729SendMode | O | Integer | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | O | Integer | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| sipG723Annexa | O | Integer | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | O | Boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | O | Vector<String> | H323 音频/视频列表 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipCodecAssign | O | Boolean | true: 限制 SIP  音频/ 视频编码为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | O | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | O | Boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | O | Boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | O | Boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| feerateRestrict | O | Boolean | true:校验被叫号码费率 false:不校验费率 |
| leastCostRouting | O | Boolean | 最低秒费率排序（在 feerateRestrict 为 true 时有效） true:启用 false:关闭 |
| minProfitPercentEnable | O | Boolean | feerateRestrict 为 true 时有效 是否开启最低利润率限制 |
| minProfitPercent | O | Integer | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | O | Boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | O | Double | 最高秒费率值（若分钟费率为 0.6， 此值应该设置为 0.01） |
| enablePhoneDisplay | O | Boolean | true:主叫为话机时使用话机的去电 显示作为主叫号码 false:主叫为话机时使用话机的号码 显示作为主叫号码 |
| clearingAccountUseCallou tE164 | O | Boolean | true:使用拨号规则后的被叫号码作 为结算账户计费被叫 false:使用拨号规则前的被叫号码作 为结算账户计费被叫 |
| softswitchName | O | String | 软交换名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| forwardSignalRewriteE164 GroupEnable | O | Boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |
| forwardSignalRewriteE164 Group | O | String | 呼叫前转信令改使用的号码群组名 称 |
| memo | O | String | 备注 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| externalNumberVerifyBits | O | Long | 智能黑名单，该参数采用 bit  位控 制，每一位表示开启某项功能 1<<0:开启智能黑名单 1<<1:保险营销 1<<2:股票推荐 1<<3:房产新盘 1<<4:教育培训 1<<5:M0/M1 催收 1<<6:房产中介 1<<7:问卷调查 1<<8:车险回访 1<<9:客服通知 1<<10:金融营销   1<<11:语音验证码 |
| externalNumberVerifyRew riteCaller | O | String | 智能黑名单主叫拨号规则 |
| externalNumberVerifyRew riteCallee | O | String | 智能黑名单被叫拨号规则 |
| scheduledCallinPrefixes | O | InfoScheduledCallinPrefix es[] | 时段呼叫限制 |
| rewriteRulesInCallerUseE1 64GroupEnable | O | Boolean | 主叫号码池 false：关闭 true：启用 |
| rewriteRulesInCallerUseE1 64Group | O | String | 主叫号码池 号码组组名称 |
| rewriteRulesInCallerUseE1 64Line | O | Integer | 主叫号码池号码复用次数 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| signalPortLocal | O | Integer | 信令本地端口 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.18 删除落地网关
接口地址/external/server/DeleteGatewayRouting
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 落地网关名称 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.19 查询落地网关
接口地址/external/server/GetGatewayRouting
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | M | String [] | 网关名称 不设置表示获取所有对接网关信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoGatewayRoutings | O | InfoGatewayRouting [] | 话机信息 |

类型 InfoGatewayRouting 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 落地网关名称 |
| prefix | M | String | 落地网关前缀（可使用逗号分隔） |
| prefixStyle | M | int | 前缀匹配方式 0:终结模式 1:延续模式 |
| password | M | String | 落地网关注册密码 |
| customerPassword | M | String | 落地网关 web 查询密码 |
| gatewayGroups | M | String | 所属网关群组（逗号分隔多个群组 名称） |
| capacity | M | int | 线路上限 |
| lockType | M | int | 锁定类型 0:无锁定 3:全部锁定 |
| priority | M | int | 优先级 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| registerType | M | int | 注册类型 0:静态 1:动态 2:注册（向其他平台进行注册） 3:IMS 边缘设备 |
| remoteIp | M | String | 落地网关远端地址 |
| rtpForwardType | M | int | 媒体转发类型 0:自动 1:开启 2:关闭 3:必须开启 |
| encrypt | M | boolean | true:加密 false:不加密 |
| protocol | M | int | 信令协议 0:H323 1:SIP |
| signalPort | M | int | 信令端口 |
| localIp | M | String | 本地地址 空:表示由系统自行选择本地地址 |
| mediaCheckDirection | M | int | 媒体中断检测（仅在通话进行了媒 体转发时有效） 0:不检测 1:检测是否有媒体报文传输给远端 2:检测是否收到来自远端的媒体报 文 3:检测远端与本地有双向的媒体报 文 |
| maxCallDurationLower | M | int | 大于 0:最长通话时间下限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationUpper 保持一致） 0:      无   限  制   （   需  与 maxCallDurationUpper 保持一致） |
| maxCallDurationUpper | M | int | 大于 0:最长通话时间上限 -1: 使 用 系 统 参 数 值 （需 与 maxCallDurationLower 保持一致） 0:      无   限  制   （   需  与 maxCallDurationLower 保持一致） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeE164Restrict | M | int | 被叫号码限制 0:不限制 1:限制被叫号码必须是平台存在的 话机号码 2:限制被叫号码必须不是平台存在 的话机号码 |
| callerE164CheckEnable | M | boolean | true:检查主叫号码规范性 false:不检查主叫号码规范性 |
| callerE164CheckCity | M | boolean | true:允许主叫号码为城市号码 false:不允许主叫号码为城市号码 |
| callerE164CheckMobile | M | boolean | true:允许主叫号码为移动号码 false:不允许主叫号码为移动号码 |
| callerE164CheckOther | M | boolean | true:允许主叫号码为非城市号码与 非移动号码 false:不允许主叫号码为非城市号码 与非移动号码 |
| calleeE164CheckEnable | M | boolean | true:检查被叫号码规范性 false:不检查被叫号码规范性 |
| calleeE164CheckCity | M | boolean | true:允许被号码为城市号码 false:不允许被叫号码为城市号码 |
| calleeE164CheckMobile | M | boolean | true:允许被叫号码为移动号码 false:不允许被叫号码为移动号码 |
| calleeE164CheckOther | M | boolean | true:允许被叫号码为非城市号码与 非移动号码 false:不允被主叫号码为非城市号码 与非移动号码 |
| callinCallerPrefixesAllow | M | boolean | true:允许 callinCallerPrefixes 设置的 前缀列表作为主叫号码前缀 false:禁止 callinCallerPrefixes  设置 的前缀列表作为主叫号码前缀 |
| callinCallerPrefixes | M | LongString | 主叫号码限制功能中主叫号码前缀 列表（可使用逗号分隔） |
| callinCalleePrefixesAllow | M | boolean | true:允许callinCalleePrefixes 设置的 前缀列表作为被叫号码前缀 false:禁止 callinCalleePrefixes  设置 的前缀列表作为被叫号码前缀 |
| callinCalleePrefixes | M | LongString | 被叫号码限制功能中被叫号码前缀 列表（可使用逗号分隔） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callinForwardPrefixesAllo w | M | boolean | true:允许 callinForwardPrefixes 设置 的前缀列表作为前转号码前缀 false:禁止 callinForwardPrefixes  设 置的前缀列表作为前转号码前缀 |
| callinForwardPrefixes | M | LongString | 前转号码限制功能中前转号码前缀 列表（可使用逗号分隔） |
| rewriteRulesInCaller | M | LongString | 主叫拨号规则 |
| rewriteRulesInCallee | M | LongString | 被叫拨号规则 |
| rewriteRulesInMobileArea Allow | M | boolean | true:开启 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 false:关闭 rewriteRulesInMobileArea 所设置的区号对应城市的移动号码 添加区号 |
| rewriteRulesInMobileArea | M | LongString | 移动号码需添加区号的地区（可使 用逗号分隔） |
| timeoutSetup | M | int | H323 Setup 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceeding | M | int | H323  CallProceeding 超时时间（单 位:秒） 0:表示使用系统参数设定值 |
| timeoutCallProceedingOlc | M | int | H323   CallProceeding   包 含 Open   Logical Channel 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutAlerting | M | int | H323 Alerting 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutInvite | M | int | SIP Invite 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutTrying | M | int | SIP Trying 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgressSd p | M | int | SIP  SessionProgress 含 SDP 超时时 间（单位:秒） 0:表示使用系统参数设定值 |
| timeoutSessionProgress | M | int | SIP SessionProgress 超时时间（单位: 秒） 0:表示使用系统参数设定值 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| timeoutRinging | M | int | SIP Ring 超时时间（单位:秒） 0:表示使用系统参数设定值 |
| denyCallerCalleeAllow | M | boolean | true:允许 denyCallerCallee 设置的主 叫向对应被叫进行呼叫 false:禁止 denyCallerCallee  设置的 主向叫对应被叫进行呼叫 |
| denyCallerCallee | M | LongString | 主叫向对应被叫进行呼叫的限制列 表格 式 为 [< 主 叫 号码>:< 被 叫 号 码>[,<主叫号码>:<被叫号码>]…]    例如:025:010,021:023 |
| denySameCityCodesAllow | M | boolean | true:允许 denySameCityCodes  设置 的区号进行同城呼叫 false:禁止 denySameCityCodes 设置 的区号进行同城呼叫 |
| denySameCityCodes | M | LongString | 同城呼叫功能限制的城市区号列表 （使用逗号分隔多个区号） |
| checkMobileAreaAllow | M | boolean | true:允许呼叫 checkMobileArea  设 置的区号对应城市的移动号码 false:禁止呼叫 checkMobileArea 设 置的区号对应城市的移动号码 |
| checkMobileArea | M | LongString | 移动号码呼叫功能限制的城市区号 列表（使用逗号分隔多个区号） |
| switchAllowRing | O | Boolean | 收到振铃信令 18x 后的网关切换方 式 false:禁止 true:允许 |
| switchAllowSdp | O | Boolean | SIP 协议时，当信令内包含 Sdp 时 的后续处理方式 false:禁止 true:允许 |
| switchAllowRtp | O | Boolean | 当在媒体转发时收到来自远端的媒 体报文时的后续处理方式 false:禁止 true:允许 |
| switchAllowBusy | O | Boolean | 当收到被叫忙后的后续处理方式 false:禁止 true:允许 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| switchAllowErrorCode | O | Boolean | 收到列表内错误码，后续网关切换 方式 false:禁止 true:允许 |
| sipResponseAddressMetho d | M | int | SIP Response 信令的地址 0:回应至原始请求的地址 1:回应至原始请求的 IP，但端口使 用 Via 头部中标识的端口 2:回应至 Via 头部中标识的地址 |
| sipRequestAddressMethod | M | int | SIP Request 信令的地址 0:请求至原始请求的地址 1:请求至原始请求的 IP，但端口使 用 Contact 头部中标识的端口 2:请求至Contact 头部中标识的地址 |
| dtmfSendMethodH323 | M | int | H323 协议，软交换发送 DTMF 方 式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 60:关闭 |
| dtmfSendMethodSIP | M | int | SIP 协议，软交换发送 DTMF 方式 0:自动 10:RFC2833 50:SIP Info 60:关闭 |
| dtmfReceiveMethod | M | int | 软交换接收主叫 DTMF 方式 0:所有 10:RFC2833 20:信令 30:关闭 |
| dtmfSendPayloadTypeH32 3 | M | int | Dtmf 为 RFC2833 在H323 协议时使 用的 Payload Type |
| dtmfSendPayloadTypeSIP | M | int | Dtmf为RFC2833 在 SIP 协议时使用 的 Payload Type |
| dtmfReceivePayloadType | M | int | Dtmf 为 RFC2833 软交换接收 Dtmf 信号使用的 Payload Type |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| q931NumberingPlan | M | int | Q931NumberingPlan -1:默认，使用系统参数设定 0:UnknownPlan 1:ISDNPlan 3:DataPlan 4:TelexPlan 8:NationalStandardPlan 9:PrivatePlan 15:ReservedPlan |
| q931NumberType | M | int | Q931NumberType -1:默认，使用系统参数设定 0:UnknownType 1:InternationalType 2:NationalType 3:NetworkSpecificType 4:SubscriberType 6:AbbreviatedType 7:ReservedType |
| q931PresentationIndicator | M | int | Q931PresentationIndicator -1:默认，使用系统参数设定 0:Presentation allowed 1:Presentation restricted 2:Number    not    available    due    to interworking 3:Reserved 4:无 |
| q931ScreeningIndicator | M | int | Q931ScreeningIndicator -1:默认，使用系统参数设定 0:User-provided ，not screened 1:User-provided ，verified and passed 2:User-provided ，verified and failed  3:Network provided 4:无 |
| clearingAccount | M | String | 结算账户名称 |
| h323FastStart | M | boolean | true:启用 H323 的 fast start 功能 false:关闭 H323 的 fast start 功能 |
| h323H245Tunneling | M | boolean | true:启用H323 的 H245 tunneling 功 能 false:关闭 H323  的 H245  tunneling 功能 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| h323H245InSetup | M | boolean | true:在 H323  的 Setup  信令中包含 H245 信令 false:在H323 的 Setup 信令中不包含 H245 信令 |
| h323T38 | M | boolean | true:H323 协议时支持 T38 信令 false:H323 协议时忽略 T38 信令 |
| sipTimer | M | boolean | true:支持 SIP Timer 协议（RFC4028） false:禁止 SIP Timer 协议 |
| sip100Rel | M | boolean | true:支持 SIP 100rel 协议 false:禁止 SIP 100rel 协议 |
| sipT38 | M | boolean | true:支持 SIPT38 协议 false:禁止 SIPT38 协议 |
| sipDisplay | M | boolean | true: 在 向 远 端 发 送 信 令 时 包 含 Display  头部 false:在向远端发送信 令时不包含 Display 头部 |
| sipRemotePartyId | M | boolean | true: 在 向 远 端 发 送 信 令 时 包 含 RemotePartyId 头部 false:在向远端发送信令时不包含 RemotePartyId 头部 |
| sipPrivacy | O | Integer | 0:无 1:透传 2:id 3:none |
| sipPPreferredIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| sipPAssertedIdentity | O | Integer | 0:无 1:透传 2:主叫号码 |
| groupE164Change | M | boolean | true:启用号码变换功能 false:关闭号码变换功能 |
| callerAllowLength | M | int | 主叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeAllowLength | M | int | 被叫号码允许的号码长度掩码 0:表示允许所有长度 1<<x:表示允许长度为 x  的号码（x 小于 32） |
| callerLimitE164GroupsAll ow | M | boolean | true:允许 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 false:禁止 callerLimitE164Groups 所 设置的号码组作为主叫号码呼叫 |
| callerLimitE164Groups | M | String | 主叫号码组列表（可使用逗号分隔） |
| calleeLimitE164GroupsAll ow | M | boolean | true:允许 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 false:禁止 calleeLimitE164Groups 所 设置的号码组作为被叫号码呼叫 |
| calleeLimitE164Groups | M | String | 被叫号码组列表（可使用逗号分隔） |
| h323G729SendMode | M | int | H323 G729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729SendMode | M | int | SIPG729 协商模式 0:自动 1:将 G729a 与 G729  当作 G729  协 商 2:将 G729a 与 G729  当作 G729a  协 商 3:将 G729  或 G729  作为 G729  与 G729a 进行协商 |
| sipG729Annexb | M | int | G729 annexb 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| sipG723Annexa | M | int | G723 annexa 参数填写方式 0:自动 1:annex=yes 2:annex=no 3:无 annex 4:透传对端的 annex |
| h323CodecAssign | M | boolean | true:限制 H323  音频/视频编码为 h323Codecs 设定值 false:软交换自动协商 |
| h323Codecs | M | Vector<String> | H323 音频/视频列表 |
| sipCodecAssign | M | boolean | true: 限制 SIP  音频/ 视频编码为 SIPCodecs 设定值 false:软交换自动协商 |
| sipCodecs | M | Vector<String> | SIP 音频/视频列表 |
| audioCodecTranscodingEn able | M | boolean | true:允许使用编码转换 false:不允许使用编码转换 |
| rtpIncludeDtmfInband | M | boolean | true:媒体包含带内(inband)DTMF false:   媒 体 不 包 含 带  内 (inband)DTMF |
| rtpNeedDtmfInband | M | boolean | true:需使用带内(inband)DTMF 发送 false:   不 额 外 使 用 带  内 (inband)DTMF 发送 |
| feerateRestrict | M | boolean | true:校验被叫号码费率 false:不校验费率 |
| leastCostRouting | M | boolean | 最低秒费率排序（在 feerateRestrict 为 true 时有效） true:启用 false:关闭 |
| minProfitPercentEnable | M | boolean | feerateRestrict 为 true 时有效 是否开启最低利润率限制 |
| minProfitPercent | M | int | 最低利润率限制若设置为 10  表示 利润率为 10% 取值范围-10000 至 10000 |
| maxSecondRatesEnable | M | boolean | 最高秒费率限制 true:开启 false 关闭 |
| maxSecondRates | M | double | 最高秒费率值 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| enablePhoneDisplay | M | boolean | true:主叫为话机时使用话机的去电 显示作为主叫号码 false:主叫为话机时使用话机的号码 显示作为主叫号码 |
| clearingAccountUseCallou tE164 | M | boolean | true:使用拨号规则后的被叫号码作 为结算账户计费被叫 false:使用拨号规则前的被叫号码作 为结算账户计费被叫 |
| softswitchName | O | String | 软交换名称 未设置:表示不属于任何软交换 空串:表示属于所有软交换 |
| forwardSignalRewriteE164 GroupEnable | O | Boolean | true:开启呼叫前转信令拨号规则 false:关闭呼叫前转信令拨号规则 |
| forwardSignalRewriteE164 Group | O | String | 呼叫前转信令改使用的号码群组名 称 |
| memo | O | String | 备注 |
| dynamicBlackListInStanda lone | O | Boolean | 独立模式下启用动态黑名单 true:开启 false:关闭 |
| mediaRecord | O | Boolean | 录音 true:开启 false:关闭 |
| externalNumberVerifyBits | O | Long | 智能黑名单，该参数采用 bit  位控 制，每一位表示开启某项功能 1<<0:开启智能黑名单 1<<1:保险营销 1<<2:股票推荐 1<<3:房产新盘 1<<4:教育培训 1<<5:M0/M1 催收 1<<6:房产中介 1<<7:问卷调查 1<<8:车险回访 1<<9:客服通知 1<<10:金融营销   1<<11:语音验证码 |
| externalNumberVerifyRew riteCaller | O | String | 智能黑名单主叫拨号规则 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| externalNumberVerifyRew riteCallee | O | String | 智能黑名单被叫拨号规则 |
| scheduledCallinPrefixes | O | InfoScheduledCallinPrefix es[] | 时段呼叫限制 |
| rewriteRulesInCallerUseE1 64GroupEnable | O | Boolean | 主叫号码池 false：关闭 true：启用 |
| rewriteRulesInCallerUseE1 64Group | O | String | 主叫号码池 号码组组名称 |
| rewriteRulesInCallerUseE1 64Line | O | Integer | 主叫号码池号码复用次数 |
| signalPortLocal | O | Integer | 信令本地端口 |
| calculateRouteQuality | O | Integer | 实时计算路由质量 0：默认 1：开启 2：关闭 |

3.20 查询在线落地网关
接口地址/external/server/GetGatewayRoutingOnline
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | O | String [] | 对接网关名称 不设置:表示此过滤条件无效 |
| softswitchName | O | String | 软交换名称 不设置:表示此过滤条件无效，查询 所有的软交换 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoGatewayRoutingOnlin es | O | InfoGatewayRoutingOnlin e [] | 套餐订单列表 |

类型 InfoGatewayRoutingOnline 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 落地网关 ID |
| name | M | String | 落地网关名称 |
| prefix | M | String | 落地网关前缀 |
| currentCall | M | int | 当前呼叫总数 |
| capacity | M | int | 呼叫线路上限 |
| asr | M | double | 呼叫应答率 |
| responseRatio | M | double | 呼叫回应率 |
| connectedRatio | M | double | 呼叫接通率 |
| acd | M | long | 平均通话时长（单位:秒） |
| remoteIp | M | String | 远端地址 |
| natIp | O | String | NAT 内部地址，仅在网关与软交换 间存在地址转换设备时有效 |
| localIp | M | String | 注册本地地址 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| registerTime | M | long | 注册时间（UTC 1970-01-01 至今的 毫秒数） 0:静态网关 |
| updateTime | M | long | 上次更新时间（UTC 1970-01-01 至 今的毫秒数） 0:静态网关 |
| keepTime | M | long | 在线时间（单位:秒） 0:静态网关 |
| cryptoType | M | int | 加密类型 0:未加密 1:RC4 |
| registerName | O | String | 向其他平台注册的标识，仅在网关 类型为注册时有效 |
| retryAfter | M | long | 网关禁用时长(毫秒)，禁用是由于落 地网关回应 Retry-After 头域造成的 |
| softswitchName | M | String | 软交换名称 |
| softswitchIp | M | String | 软交换 IP |

3.21 查询当前通话
接口地址/external/server/GetCurrentCall
该接口不建议频繁使用，过于频繁的调用可能导致系统性能低下
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164s | O | String [] | 主叫号码 不设置:表示此过滤条件无效 |
| calleeE164s | O | String [] | 被叫号码 不设置:表示此过滤条件无效 |
| gatewayMappingName | O | String | 对接网关 不设置:表示此过滤条件无效 |
| gatewayRoutingName | O | String | 落地网关 不设置:表示此过滤条件无效 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoCurrentCalls | O | InfoCurrentCall [] | 当前通话列表 |

类型 InfoCurrentCall 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164 | M | String | 主叫号码 |
| calleeE164 | M | String | 被叫号码 |
| callerGatewayId | M | String | 主叫网关 |
| calleeGatewayId | M | String | 被叫网关 |
| connectedTime | M | long | 呼叫接通时间 当未接通时表示呼叫接入时间 （UTC 1970-01-01 至今的毫秒数） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| keepTime | M | long | 大于等于 0:呼叫持续时长（单位:毫 秒） -1:呼叫初始化（Setup） -2:呼叫接续中（CallProceeding） -3: 呼 叫 接 续 中 （ CallProceeding （RTP）） -4:呼叫接续中（Progress） -5:振铃（Alerting） -6:接通（Connet） -7:呼叫初始化（Invite） -8:呼叫接续中（Trying） -9:呼叫接续中（SessionProgress） -10: 呼 叫接续 中（ SessionProgress （SDP）） -11:振铃（Ringing） -12:接通（Ok） -13:挂断（Release） -14:呼叫转移中（Transfering） -15:呼叫转移成功（TransferOk） -16:呼叫转移失败（TransferFailed） -17:放弃呼叫转移（TransferCancel） |
| callCodec | M | String | 呼叫编码 |
| callerCodec | M | String | 主叫编码集 |
| calleeCodec | M | String | 被叫编码集 |
| callerRtpIp | M | String | 主叫 Rtp 地址信息（含音频与视频） |
| calleeRtpIp | M | String | 被叫 Rtp 地址信息（含音频与视频） |
| callerReceiveDtmf | M | int | 软交换接收主叫 DTMF 方式 0:自动 10:RFC2833 20:H.245 alphanumeric 30:H.245 signal 40:Q.931 keypad 50:SIP Info 60:关闭 |
| callerSendDtmf | M | int | 软交换发送给主叫的 DTMF 方式， 取值同 callerReceiveDtmf |
| calleeReceiveDtmf | M | int | 软交换接受被叫 DTMF 方式，取值 同 callerReceiveDtmf |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeSendDtmf | M | int | 软交换发送给被叫的 DTMF 方式， 取值同 callerReceiveDtmf |
| callerInfoRtpFlowAudio | M | InfoRtpFlow | 主叫语音流量信息 |
| calleeInfoRtpFlowAudio | M | InfoRtpFlow | 被叫语音流量信息 |
| callerInfoRtpFlowVideo | M | InfoRtpFlow | 主叫视频流量信息 |
| calleeInfoRtpFlowVideo | M | InfoRtpFlow | 被叫视频流量信息 |
| callerTerminal | M | String | 主叫设备名称 |
| calleeTerminal | M | String | 被叫设备名称 |
| callerCryptoType | M | int | 主叫加密类型 0:未加密 1:RC4 |
| calleeCryptoType | M | int | 被叫加密类型 0:未加密 1:RC4 |
| callerLocalIp | M | String | 主叫信令本地地址 |
| calleeLocalIp | M | String | 被叫信令本地地址 |
| callId | M | int | 呼叫在软交换中的唯一标识 |

InfoRtpFlow 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| rtpPackets | M | int | 接受报文数量 |
| rtpBytes | M | int | 接收字节数量 |
| rtpDuration | M | long | 持续时间（单位:微秒） |

3.22 充值
接口地址/external/server/Pay
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ownerName | M | String | 充值对象名称 |
| ownerType | M | int | 充值对象名称类型 2:账户 6:平台话机 11:在用电话卡卡号 25:绑定号码 44:对接网关 |
| money | M | double | 充值金额 |
| memo | O | String | 充值备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPay | O | InfoPay | 缴费历史记录 |

InfoPay 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户名称 |
| money | M | double | 账户余额 |
| validTime | M | long | 有效期（UTC 1970-01-01 至今的毫 秒数 ） |
| payMoney | M | double | 充值金额 |

3.23 创建套餐
接口地址/external/server/CreateSuite
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 套餐名称 |
| rentPeriod | M | int | 租用周期（需大于 0） |
| rentType | M | int | 租用类型 0:天 1:月 2:年 3:一次性(rentPeriod  含义变更为可 用秒数) |
| nonholonomicOrder | M | boolean | true:允许非完整订阅 false:不允许非完整订阅 |
| rentFee | M | double | 租金 |
| minConsumption | M | double | 最低消费额 |
| lowerConsumption | M | double | 生效消费下限 |
| giftMoney | M | double | 赠送金额 |
| infoGiftTimes | O | InfoGiftTime [] | 赠送时长 |
| memo | O | String | 备注 |

InfoGiftTime  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| prefix | M | LongString | 地区前缀（可使用逗号分隔多个前 缀） |
| startTime | M | int | 一 天 的 起 始 时 间 （取 值 范 围 0-86400），该时间为与当日 0 点的 偏差秒数 |
| endTime | M | int | 一 天 的 终 止 时 间 （取 值 范 围 0-86400），该时间为与当日 0 点的 偏差秒数 |
| giftTime | M | int | 赠送的秒数 |
| billingTime | M | int | 赠送时长的计费周期 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| id | O | Integer | 套餐 Id |

3.24 删除套餐
接口地址/external/server/DeleteSuite
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 套餐 Id |
| force | O | int | 0:不强制删除，需检查依赖关系（默 认） 1:强制删除，并取消依赖关系 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.25 查询套餐
接口地址/external/server/GetSuite
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ids | O | int [] | 套餐 Id 数组，当不设置此值时，表 示获取所有套餐信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoSuites | O | InfoSuite [] | 套餐信息 |

InfoSuite 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 套餐 Id |
| name | M | String | 套餐名称 |
| rentPeriod | M | int | 租用周期 |
| rentType | M | int | 租用类型 0:天 1:月 2:年 3:一次性(rentPeriod  含义变更为可 用秒数) |
| nonholonomicOrder | M | boolean | true:允许非完整订阅 false:不允许非完整订阅 |
| rentFee | M | double | 租金 |
| minConsumption | M | double | 最低消费额 |
| lowerConsumption | M | double | 生效消费下限 |
| giftMoney | M | double | 赠送金额 |
| infoGiftTimes | O | InfoGiftTime [] | 赠送时长 |
| memo | O | String | 备注 |

3.26 创建套餐订单
接口地址/external/server/CreateSuiteOrder
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ownerName | M | String | 所有者名称 |
| ownerType | M | int | 所有者类型 2:账户 6:话机 |
| suiteId | M | int | 套餐 Id |
| availableTime | M | long | 生效时间（UTC 1970-01-01 至今的 毫秒数，需为服务器时区的 0 点） 0:表示生效时间为服务器时区当日 0 点，并立即生效 |
| expireTime | O | Long | 失效时间（GMT 1970-01-01 至今的 毫秒数 ） 不选或 9223372036854775807 表示 无限制 当套餐 rentType 为“一次性”时:若不 设置此值，则一次性套餐的失效时 间 为 :availableTime    +    套 餐 的 rentPeriod *1000;若设置此值则根据 此值设定失效时间，对于一次性套 餐，一旦创建订单即转换为生效套 餐，订单自动删除 |
| priority | O | Integer | 优先级 不设置或 2147483647  表示无优先 级 |
| failedProcessMode | O | Integer | 当账户余额不足以支付租金时的处 理模式 0（默认）:等待下次充值 1:等待下一个租用周期（仅在套餐 租用单位为日或月时有效） 2:删除 |
| rentPercent | O | Double | 租金百分比 默认值:100 |
| memo | O | String | 订单备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| id | O | Integer | 成功后返回创建套餐订单的 id |

3.27 修改套餐订单
接口地址/external/server/ModifySuiteOrder
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 套餐订单 id |
| expireTime | O | Long | 失效时间（UTC 1970-01-01 至今的 毫秒数，需为服务器时区的 0 点） 9223372036854775807:表示无限制 |
| priority | O | Integer | 优先级 不设置或 2147483647  表示无优先 级 |
| failedProcessMode | O | Integer | 当账户余额不足以支付租金时的处 理模式 0（默认）:等待下次充值 1:等待下一个租用周期（仅在套餐 租用单位为日或月时有效） 2:删除 |
| rentPercent | O | Double | 租金百分比 |
| memo | O | String | 订单备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.28 删除套餐订单
接口地址/external/server/DeleteSuiteOrder
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 套餐订单的 id |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.29 查询套餐订单
接口地址/external/server/GetSuiteOrder
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ownerName | M | String | 所有者名称 |
| ownerType | M | int | 所有者类型 2:账户 6:话机 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoSuiteOrders | O | InfoSuiteOrder [] | 套餐订单列表 |

InfoSuiteOrder 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 套餐订单 Id |
| suiteId | M | int | 套餐 Id |
| availableTime | M | long | 生效时间（UTC 1970-01-01 至今的 毫秒数） |
| expireTime | M | long | 失效时间（UTC 1970-01-01 至今的 毫秒数） 另:9223372036854775807 表示无限制 |
| priority | M | int | 优先级 |
| rentPercent | M | double | 租金百分比 |
| memo | M | String | 订单备注 |

3.30 查询生效套餐
接口地址/external/server/GetCurrentSuite
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ownerName | M | String | 所有者名称 |
| ownerType | M | int | 所有者类型 2:账户 6:话机 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoCurrentSuites | O | InfoCurrentSuite [] | 套餐订单列表 |

类型 InfoCurrentSuite 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 生效套餐 Id |
| suiteId | M | int | 套餐 Id |
| suiteOrderId | M | int | 套餐订单 Id |
| rentPeriod | M | int | 租用周期 |
| rentType | M | int | 租用类型 0:天 1:月 2:年 3:一次性(rentPeriod  含义变更为可 用秒数) |
| rentFee | M | double | 租金 |
| expireTime | M | long | 失效时间 （UTC 1970-01-01 至今的毫秒数） |
| minConsumption | M | double | 最低消费额 |
| currentConsumption | M | double | 周期内消费 |
| lowerConsumption | M | double | 生效消费下限 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| giftMoney | M | double | 赠送金额 |
| infoGiftTimes | O | InfoGiftTime [] | 赠送时长 |
| memo | O | String | 备注 |

3.31 删除生效套餐
接口地址/external/server/DeleteCurrentSuite
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 生效套餐 Id |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.32 创建在用电话卡
接口地址/external/server/CreateActivePhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 卡号 |
| account | M | String | 在用电话卡所属账户 |
| password | O | String | 密码 |
| displayE164 | O | String | 去电显示 |
| bindLimit | O | Integer | 绑定号码上限 不设置:表示无限制 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| password | O | Integer | 当创建请求未设置密码时，系统自 动生成随机密码 |

3.33 修改在用电话卡
接口地址/external/server/ModifyActivePhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 卡号 |
| account | O | String | 在用电话卡所属账户 |
| password | O | String | 密码 |
| displayE164 | O | String | 去电显示 |
| bindLimit | O | Integer | 绑定号码上限 不设置:表示无限制 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.34 删除在用电话卡
接口地址/external/server/DeleteActivePhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 卡号 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.35 查询在用电话卡
接口地址/external/server/GetActivePhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pins | O | String [] | 卡号列表(若 accounts 不设置则此参 数必选) |
| accounts | O | String [] | 账户号码列表(若 pins  不设置则此 参数必选) |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoActivePhoneCards | O | InfoActivePhoneCard [] | 在用电话卡信息 |

InfoActivePhoneCard 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 卡号 |
| account | M | String | 在用电话卡所属账户 |
| password | M | String | 密码 |
| displayE164 | M | String | 去电显示 |
| bindLimit | M | int | 绑定号码上限 不设置:表示无限制 |
| activeTime | M | long | 激活时间（UTC 1970-01-01 至今的 毫秒数 ） |
| memo | M | String | 备注 |

3.36 创建绑定号码
接口地址/external/server/CreateBindedE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 绑定号码 |
| pin | M | String | 卡号 |
| displayE164 | O | String | 去电显示 |
| rewriteRulesOutCallee | O | LongString | 呼出拨号规则 |
| language | O | String | 语言 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.37 修改绑定号码
接口地址/external/server/ModifyBindedE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 绑定号码 |
| pin | O | String | 卡号 |
| displayE164 | O | String | 去电显示 |
| rewriteRulesOutCallee | O | LongString | 呼出拨号规则 |
| language | O | String | 语言 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.38 删除绑定号码
接口地址/external/server/DeleteBindedE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 绑定号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.39 查询绑定号码
接口地址/external/server/GetBindedE164
**请求格式**
包含参数必选其一
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164s | O | String [] | 绑定号码列表 |
| pin | O | String | 在用电话卡卡号 |
| account | O | String | 账户号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoBindedE164s | O | InfoBindedE164 [] | 绑定号码信息 |

InfoBindedE164 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 绑定号码 |
| pin | M | String | 卡号 |
| account | M | String | 在用电话卡所属账户 |
| displayE164 | M | String | 去电显示 |
| rewriteRulesOutCallee | M | LongString | 呼出拨号规则 |
| bindTime | M | long | 绑定时间（UTC 1970-01-01 至今的 毫秒数 ） |
| language | M | String | 语言 |
| memo | M | String | 备注 |

3.40 查询费率组
接口地址/external/server/GetFeeRateGroup
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | O | String [] | 费率组名称列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoFeeRateGroups | O | InfoFeeRateGroup [] | 费率组信息 |

InfoFeeRateGroup 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 费率组名称 |
| memo | M | String | 备注 |

3.41 创建费率组
接口地址/external/server/CreateFeeRateGroup
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 费率组名称 |
| fakeMinute | O | Integer | 电话卡 60 秒等效时长 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.42 修改费率组
接口地址/external/server/ModifyFeeRateGroup
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 费率组名称 |
| fakeMinute | O | Integer | 电话卡 60 秒等效时长 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.43 删除费率组
接口地址/external/server/DeleteFeeRateGroup
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 费率组名称 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.44 查询费率
接口地址/external/server/GetFeeRate
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| feeRateGroup | M | String | 费率组名称 |
| areaCodes | O | String [] | 地区信息列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoFeeRates | O | InfoFeeRate [] | 费率信息 |

InfoFeeRate 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| feePrefix | M | String | 费率前缀 |
| areaCode | M | String | 地区前缀 |
| type | M | int | 费率类型 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |
| areaName | M | String | 地区名称 |
| infoFeeRateSections | M | InfoFeeRateSection [] | 分段费率 |
| fee | M | double | 计费费率 |
| period | M | int | 计费周期 |
| lockType | M | int | 锁定类型 0:无锁定 1:锁定 |
| ivrFee | M | double | 电话卡提示费率 |
| ivrPeriod | M | int | 电话卡提示计费周期 |

InfoFeeRateSection 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| fee | M | double | 金额 |
| time | M | int | 计费时长 |
| position | M | int | 序号 |

3.45 查询号码变换表
接口地址/external/server/GetE164Convert
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户号码 |
| e164 | O | String | 电话号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoE164Converts | O | InfoE164Convert [] | 缴费历史记录 |

InfoE164Convert  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 唯一标识 |
| account | M | String | 账户名称 |
| e164 | M | String | 电话号码 |
| mappingGatewayCallerE1 64 | M | String | 对接网关呼入主叫号码 |
| routingGatewayCalleeE16 4 | M | String | 落地网关呼出被叫号码 |
| memo | M | String | 缴费后账户余额 |

3.46 查询缴费记录
接口地址/external/server/GetPayHistory
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户号码（当 agentAccount 不设置 时，此参数必须设置） |
| agentAccount | O | String | 代理商账户号码（当 account 不设置 时，此参数必须设置） |
| beginTime | M | String | 开始时间 格式:yyyyMMddHHmmss |
| endTime | M | String | 终止时间 格式:yyyyMMddHHmmss |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPayHistorys | O | InfoPayHistory[] | 缴费历史记录 |

InfoPayHistory 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户名称 |
| fee | M | double | 缴费金额 |
| type | M | int | 类型 0:充值 1:扣费 2:开户 3:归零 |
| payType | M | int | 方式 0:现金 2:充值卡 5:其他 |
| customerMoney | M | double | 缴费后账户余额 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| payTime | M | long | 缴费时间（UTC 1970-01-01 至今的 毫秒数 ） |
| memo | M | String | 备注 |

3.47 查询历史话单
接口地址/external/server/GetCdr
该接口设计目的主要用于第三方账务处理使用，由于性能问题，不应该用于频繁操作情况
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| accounts | M | String [] | 账户号码列表 |
| callerE164 | O | String | 主叫号码 |
| calleeE164 | O | String | 被叫号码 |
| callerGateway | O | String | 主叫网关 |
| calleeGateway | O | String | 被叫网关 |
| beginTime | M | String | 开始时间 格式:yyyyMMdd |
| endTime | M | String | 终止时间 格式:yyyyMMdd |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoCdrs | O | InfoCdr [] | 话单信息 |

InfoCdr  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164 | M | String | 计费主叫号码 |
| callerAccessE164 | M | String | 呼入主叫号码 |
| callerProductId | M | String | 主叫设备名称 |
| callerToGatewayE164 | M | String | 呼出主叫号码 |
| callerGateway | M | String | 主叫网关 |
| callerip | M | String | 主叫 IP 地址 |
| calleeE164 | M | String | 计费被叫号码 |
| calleeAccessE164 | M | String | 呼入被叫被叫 |
| calleeProductId | M | String | 被叫设备名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeToGatewayE164 | M | String | 呼出被叫号码 |
| calleeGateway | M | String | 被叫网关 |
| calleeip | M | String | 被叫 IP 地址 |
| start | M | long | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） |
| stop | M | long | 终止时间（UTC 1970-01-01 至今的 毫秒数 ） |
| holdTime | M | int | 通话的时长（秒） |
| feeTime | M | int | 通话计费时长（秒） |
| fee | M | double | 账户扣费金额 |
| feePrefix | M | String | 计费地区前缀 |
| suiteFee | M | double | 套餐费用 |
| suiteFeeTime | M | int | 套餐赠送时长（秒） |
| agentFee | M | double | 代理商扣费金额 |
| agentFeeTime | M | int | 代理商计费时长（秒） |
| agentFeePrefix | M | String | 代理商计费地区前缀 |
| agentSuiteFee | M | double | 代理商套餐费用 |
| agentSuiteFeeTime | M | int | 代理商赠送时长（秒） |
| callLevel | M | int | 通话级别 1:网内通话 2:本地市话 4:国内长途 5:国际长途 |
| account | M | String | 账户号码 |
| accountName | M | String | 账户名称 |
| agentAccount | M | String | 代理商账户号码 |
| agentName | M | String | 代理商账户名称 |
| endDirection | M | int | 挂断方 0:主叫 1:被叫 2:服务器 |
| endReason | M | int | 终止原因:请参考《终止原因》说明 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| calleeBilling | M | int | 计费方式 0:主叫计费 1:被叫计费 2:外部计费 |
| billingMode | M | int | 计费模式 0:根据话机所在账户计费 1:根据对接网关所在账户计费 2:根据绑定号码所在账户计费 3:根据在用电话卡所在账户计费 |
| flowNo | M | long | 话单唯一标识 |

3.48 查询账户明细报表
接口地址/external/server/GetReportCustomerFee
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| accounts | M | String [] | 账户号码列表 |
| period | M | int | 统计周期（天） -2:按月统计 |
| beginTime | M | String | 开始时间 格式:yyyyMMdd |
| endTime | M | String | 终止时间 格式:yyyyMMdd |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoReportCustomerFees | O | InfoReportCustomerFee [] | 账户消费明细记录 |

InfoReportCustomerFee  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| beginTime | M | long | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） |
| endTime | M | long | 终止时间（UTC 1970-01-01 至今的 毫秒数 ） |
| account | M | String | 账户号码 |
| accountName | M | String | 账户名称 |
| cdrCount | M | long | 话单总计 |
| totalFee | M | double | 费用总计 |
| totalTime | M | long | 计费时长总计（秒） |
| totalSuiteFee | M | double | 套餐费用总计 |
| totalSuiteFeeTime | M | long | 套餐赠送时长总计（秒） |
| netFee | M | double | 网内通话费用 |
| netTime | M | long | 网内通话计费时长（秒） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| netCount | M | int | 网内通话数量 |
| localFee | M | double | 本地通话费用 |
| localTime | M | long | 本地通话计费时长（秒） |
| localCount | M | int | 本地通话数量 |
| domesticFee | M | double | 国内长途费用 |
| domesticTime | M | long | 国内通话计费时长（秒） |
| domesticCount | M | int | 国内通话数量 |
| internationalFee | M | double | 国际长途费用 |
| internationalTime | M | long | 国际长途计费时长（秒） |
| internationalCount | M | int | 国际长途数量 |

3.49 查询话机明细报表
接口地址/external/server/GetReportPhoneFee
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| e164s | O | String [] | 话机号码列表 |
| period | M | int | 统计周期（天） -2:按月统计 |
| beginTime | M | String | 开始时间 格式:yyyyMMdd |
| endTime | M | String | 终止时间 格式:yyyyMMdd |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoReportPhoneFees | O | InfoReportPhoneFee [] | 话机消费明细记录 |

InfoReportPhoneFee  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| beginTime | M | long | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） |
| endTime | M | long | 终止时间（UTC 1970-01-01 至今的 毫秒数 ） |
| e164 | M | String | 话机号码 |
| calleeBilling | M | int | 0:主叫计费 1:被叫计费 |
| account | M | String | 账户号码 |
| accountName | M | String | 账户名称 |
| agentAccount | M | String | 代理商账号 |
| cdrCount | M | long | 话单总计 |
| totalFee | M | double | 费用总计 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| totalTime | M | long | 计费时长总计（秒） |
| totalSuiteFee | M | double | 套餐费用总计 |
| totalSuiteFeeTime | M | long | 套餐赠送时长总计（秒） |
| netFee | M | double | 网内通话费用 |
| netTime | M | long | 网内通话计费时长（秒） |
| netCount | M | int | 网内通话数量 |
| localFee | M | double | 本地通话费用 |
| localTime | M | long | 本地通话计费时长（秒） |
| localCount | M | int | 本地通话数量 |
| domesticFee | M | double | 国内长途费用 |
| domesticTime | M | long | 国内通话计费时长（秒） |
| domesticCount | M | int | 国内通话数量 |
| internationalFee | M | double | 国际长途费用 |
| internationalTime | M | long | 国际长途计费时长（秒） |
| internationalCount | M | int | 国际长途数量 |

3.50 查询账户地区明细报表
接口地址/external/server/GetReportCustomerLocationFee
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| areaCode | O | String | 地区前缀 |
| period | M | int | 统计周期（天） -2:按月统计 |
| beginTime | M | String | 开始时间 格式:yyyyMMdd |
| endTime | M | String | 终止时间 格式:yyyyMMdd |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoReportCustomerLocati onFees | O | InfoReportCustomerLocati onFee [] | 账户地区消费明细记录 |

InfoReportCustomerLocationFee  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| beginTime | M | long | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） |
| endTime | M | long | 终止时间（UTC 1970-01-01 至今的 毫秒数 ） |
| areaCode | M | String | 地区前缀 |
| areaName | M | String | 地区名称 |
| account | M | String | 账户号码 |
| accountName | M | String | 账户名称 |
| agentAccount | M | String | 代理商账号 |
| cdrCount | M | long | 话单总计 |
| totalFee | M | double | 费用总计 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| totalTime | M | long | 计费时长总计（秒） |
| totalSuiteFee | M | double | 套餐费用总计 |
| totalSuiteFeeTime | M | long | 套餐赠送时长总计（秒） |

3.51 外部计费
接口地址/external/server/CreateCdr
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| billingMode | M | int | 计费模式 0:根据 callerE164  对应话机所在账 户计费 1:根据 callerGatewayId 对应对接网 关所在账户计费 2:根据 callerE164  对应绑定号码所 在账户计费 3:根据 callerE164  对应在用电话卡 所在账户计费 |
| account | O | String | 计费账户 不设置:系统将根据 billingMode  计 算出对应的账户 |
| callerE164 | O | String | 主叫号码 |
| calleeE164 | O | String | 被叫号码 |
| callerIp | O | String | 主叫 IP |
| callerGatewayId | O | String | 主叫经由网关 |
| callerProductId | O | String | 主叫设备名称 |
| callerToGatewayE164 | O | String | 呼出主叫 |
| calleeIp | O | String | 被叫 IP |
| calleeGatewayId | O | String | 被叫经由网关 |
| calleeProductId | O | String | 被叫设备名称 |
| calleeToGatewayE164 | O | String | 呼出被叫 |
| startTime | O | Long | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） 不设置:使用服务器当前时间 |
| stopTime | O | Long | 终止时间（UTC 1970-01-01 至今的 毫秒数 ） 不设置:使用 startTime |
| billingTime | M | int | 通话时长（通过 calleeE164 对应费 率的计费周期计算出计费时长） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| endDirection | O | Integer | 挂断方 0:主叫 1:被叫 2:服务器 |
| endReason | O | Integer | 终止原因:请参考《终止原因》说明 |
| flowNo | O | Long | -1:由系统自动产生 >=0:直接使用此值作为话单主键， 当该值与已经记录的 Cdr 发生冲突 时不进行记录与扣费。 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.52 查询账户电话簿
接口地址/external/server/GetCustomerPhoneBook
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户号码 |
| e164 | O | String | 电话号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoCustomerPhoneBooks | O | InfoCustomerPhoneBook [] | 电话簿信息 |

InfoCustomerPhoneBook 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 电话号码 |
| shortE164s | M | String[] | 短号列表 |
| name | M | String | 姓名 |
| department | M | String | 部门 |
| deviceType | M | int | 设备类型 0:无 1:移动电话 2:固定电话 3:IP 电话 |
| addressType | M | int | 地址类型 0:无 1:办公电话 2:家庭电话 |
| type | M | int | 创建类型 0:用户创建 1:自动记忆 |
| lastUpdateTime | M | long | 最 后 一 次 更 新 时 间 （ UTC 1970-01-01 至今的毫秒数） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| memo | M | String | 备注 |

3.53 创建账户电话簿
接口地址/external/server/CreateCustomerPhoneBook
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| e164 | O | String | 电    话   号    码   ，   当 infoCustomerPhoneBookOverWrite 未 设 置 时 ， 此 选 项 必 选 ， 当 infoCustomerPhoneBookOverWrite 设置时，若此项设置，表示需要更 新的电话号码 |
| infoCustomerPhoneBookO verWrite | O | InfoCustomerPhoneBookO verWrite | 采用覆盖模式创建或替换电话簿， 注意若非替换原有电话簿内容，则 电话号码是必须存在的 |
| shortE164s | O | String[] | 短号列表 |
| name | O | String | 姓名 |
| department | O | String | 部门 |
| deviceType | O | Integer | 设备类型 0:无（默认） 1:移动电话 2:固定电话 3:IP 电话 |
| addressType | O | Integer | 地址类型 0:无（默认） 1:办公电话 2:家庭电话 |
| type | O | Integer | 创建类型 0:用户创建（默认） 1:自动记忆 |
| memo | O | String | 备注 |

InfoCustomerPhoneBookOverWrite 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | O | int | 采用电话号码查找可能覆盖的原有 电话簿信息，不可与 shortE164 同时 设置 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| shortE164 | O | int | 采用短号查找可能覆盖的原有电话 簿信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.54 修改账户电话簿
接口地址/external/server/ModifyCustomerPhoneBook
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| e164 | M | String | 电话号码 |
| newE164 | O | String | 新电话号码 |
| shortE164s | O | String[] | 短号列表 |
| name | O | String | 姓名 |
| department | O | String | 部门 |
| deviceType | O | Integer | 设备类型 0:无（默认） 1:移动电话 2:固定电话 3:IP 电话 |
| addressType | O | Integer | 地址类型 0:无（默认） 1:办公电话 2:家庭电话 |
| type | O | Integer | 创建类型 0:用户创建（默认） 1:自动记忆 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.55 删除账户电话簿
接口地址/external/server/DeleteCustomerPhoneBook
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| e164s | M | String[] | 电话号码列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.56 查询软交换
接口地址/external/server/GetSoftSwitch
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoSoftSwitches | O | InfoSoftSwitch [] | 软交换信息 |

InfoSoftSwitch 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 软交换接入名称 |
| identification | M | String | 软交换标识 |
| createTime | M | long | 创建时间（UTC 1970-01-01 至今的 毫秒数 ） |
| accessTime | O | Long | 接入时间（UTC 1970-01-01 至今的 毫秒数 ） |
| accessAddress | O | String | 接入地址 |
| memo | M | String | 备注 |

3.57 查询性能
接口地址/external/server/GetPerformance
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPerformance | O | InfoPerformance | 性能信息 |

InfoPerformance 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callSize | M | int | 并发数量 |
| cdrQueueSize | M | int | 话单队列长度 |

3.58 电话卡充值
接口地址/external/server/PayByPhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ownerName | M | String | 充值对象名称 |
| ownerType | M | int | 充值对象名称类型 2:账户 6:平台话机 11:在用电话卡卡号 25:绑定号码 44:对接网关 |
| pin | M | String | 电话卡卡号 |
| password | O | String | 电话卡密码 注意:当不设置时仅校验卡号 |
| memo | O | String | 充值备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPay | O | InfoPay | 缴费历史记录 |

3.59 电话卡激活
接口地址/external/server/PhoneCardActive
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 充值卡卡号 |
| password | O | String | 充值卡密码 注意:当不设置时仅校验卡号 |
| bindedE164 | O | String | 绑定号码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.60 回拨
接口地址/external/server/CallBack
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164 | M | String | 主叫（由用户在 Web 上输入） |
| callerDisplayNumber | O | String | 主叫去电显示号码 不设置，表示采用系统默认方式 |
| calleeE164s | M | String | 被叫（平台根据企业要求设置，可 设置多个用,分隔） |
| accessE164 | M | String | 接入号码（流程所在话机号码） |
| accessE164Password | M | String | 接入号码密码（流程所在话机密码） |
| callbackBillingE164 | O | String | 回拨计费号码 ， 不设置时使用 callerE164 参数值 |
| callbackBillingPassword | O | String | 回拨计费密码 |
| calloutBillingE164 | O | String | 外呼计费号码 ， 不设置时使用 callerE164 参数值 |
| calloutBillingPassword | O | String | 外呼计费密码 |
| calloutDisplayInFrom | O | String | 外呼 Invite 内设置的 Display 号码 |
| transactionId | O | String | 提交识别码，用于本次请求与后续 状态通知、话单的对应 字符取值范围 A 至 Z ，a 至 z ，0 至 9，以及- 、_ |

**补充说明**
**回拨业务根据** accessE164 确定使用的语音业务，在使用回拨业务前需正确配置 accessE164 对应话机 的语音业务。当接入密码、回拨计费密码、外呼计费密码被设置时，则需校验对应号码的密码是否 正确。请不要将此接口直接面向终端用户开放，终端用户直接提交此接口会造成密码在网络上明文 传输，从而引发安全问题。
l 语音业务回拨计费方式
时，回拨使用 accessE164 对应话机的账 户进行计费
时，计费账户查找顺序如下
u callbackBillingE164  对应绑定号码的账户
u callbackBillingE164  对应在用电话卡卡号的账户
u callbackBillingE164  对应平台话机的账户
u accessE164 对应平台话机的账户
n
u callbackBillingE164
u callbackBillingE164
n
对应绑定号码的账户
对应在用电话卡卡号的账户
时，计费账户查找顺序如下
时，回拨使用
callbackBillingE164 对应话机的账户进行计费
l 语音业务第二路方式
n 时，回拨使用 accessE164 对应话机的账户进行计费
n 时，计费账户查找顺序如下
u calloutBillingE164  对应绑定号码的账户
u calloutBillingE164  对应在用电话卡卡号的账户
n 时，回拨使用 calloutBillingE164  对应话机的账户进行计费 **返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| transactionId | O | String | 与请求相同 与 CallStateReport  的 transactionId 一致 |
| callIdentifier | O | String | A 路呼叫唯一标识 与 CallStateReport   的 callIdentifier 一致 B 路与 A 路前缀相同，仅后续尾数 递增 |

3.61 播放语音
接口地址/external/server/PlayAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| audioes | M | String | 语音文件名称列表（使用逗号分隔 多个文件名称） |
| language | O | String | 默认使用 accessE164 对应语音流程 的语言 |
| callerDisplayNumber | O | String | 主叫去电显示号码 不设置，表示采用系统默认方式 |
| callee | M | String | 被叫号码 |
| accessE164 | M | String | 接入号码（流程所在话机号码） |
| accessE164Password | M | String | 接入号码密码（流程所在话机密码） |
| billingNumber | O | String | 计费号码 |
| billingNumberType | O | Integer | 计费号码类型 0:根据 billingNumber 对应话机所在 账户计费 2:根据 billingNumber 对应绑定号码 所在账户计费 3:根据 billingNumber 对应在用电话 卡所在账户计费 |
| transactionId | O | String | 提交识别码，用于本次请求与后续 状态通知、话单的对应 字符取值范围 A 至 Z ，a 至 z ，0 至 9，以及- 、_ |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| transactionId | O | String | 与请求相同 与 CallStateReport  的 transactionId 一致 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callIdentifier | O | String | 呼叫唯一标识 与 CallStateReport   的 callIdentifier 一致 |

3.62 获取可用通话时长
接口地址/external/server/GetAvailableTime
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| billingName | M | String | 计费主叫名称 |
| billingMode | M | int | 计费主叫类型 0:平台话机 1:对接网关 2:绑定号码 3:电话卡卡号 4:优先根据电话卡卡号找账户，其 次根据对接网关找账户 |
| calleeE164 | M | String | 被叫号码 |
| calleeEndpointType | O | Integer | 被叫号码送达的设备 0:平台话机 1:落地网关 (当为平台话机时，可对被叫号码判 断是否在特服号内，从而免计费) |
| routingGateway | O | String | 落地网关名称 |
| calleeToGatewayE164 | O | String | 落地网关拨号规则后的号码 （配合 routingGateway 一并使用， 当落地网关需要校验结算账户余额 时参数有效） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| InfoAvailableTime | O | InfoAvailableTime | 可用时长信息 |

InfoAvailableTime 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户账号 |
| accountName | O | String | 账户名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| accountMoney | O | Double | 账户余额（不包括套餐内的赠送金 额） |
| timeRemain | M | int | >0:表示可通话的秒数 <0:不可通话的原因，请参考终止原 因文档 |
| timeRemainRoutingGatew ay | O | Integer | >0:表示落地网关可通话的秒数 <0:落地网关不可通话的原因，请参 考终止原因文档 |

3.63 获取 Ivr 第二路可用通话时长
接口地址/external/server/GetIvrSecondAvailableTime
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| billingNumber | M | String | 计费主叫号码 |
| billingType | M | int | 计费主叫类型 0:接入号对应话机 1:在用电话卡 2:自动，匹配顺序为绑定号码、电 话卡卡号、平台话机号码 3:主叫号对应话机 |
| calleeE164 | M | String | 被叫号码 |
| accessE164 | O | String | 接入号 当设置此值时要求主叫账户与接入 号账户存在共同的按照流量计费的 代理商账户或各自代理商账户均无 流量计费模式。 |
| mergeBillingType | O | Integer | 叠加计费方式 0:不叠加 1:叠加接入号到第二路 2:叠加主叫号到第二路 |
| mergeE164 | O | String | 需叠加的计费号码 |
| firstE164 | M | String | 第一路的被叫号码 |
| firstConnectTime |  | long | 第 一 路 接 通 的 时 间 （ UTC 1970-01-01 至今的毫秒数） |
| firstStopTime |  | long | 第一路需计算的已经结束的时间 （UTC 1970-01-01 至今的毫秒数） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoIvrSecondAvailableTi me | O | InfoIvrSecondAvailableTi me | 可用时长信息 |

InfoIvrSecondAvailableTime 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户账号 |
| accountName | O | String | 账户名称 |
| accountMoney | O | Double | 账户余额（不包括套餐内的赠送金 额） |
| timeRemain | M | int | >0:表示可通话的秒数 <0:不可通话的原因，请参考终止原 因文档 |

3.64 查询其他收入记录
接口地址/external/server/GetConsumption
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | O | String | 账户号码（当 agentAccount 不设置 时，此参数必须设置） |
| agentAccount | O | String | 代理商账户号码（当 account 不设置 时，此参数必须设置） |
| beginTime | M | String | 开始时间 格式:yyyyMMddHHmmss |
| endTime | M | String | 终止时间 格式:yyyyMMddHHmmss |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoConsumptions | O | InfoConsumption [] | 其他收入记录 |

InfoConsumption 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| money | M | double | 消费金额 |
| customerMoney | M | double | 账户余额 |
| type | M | int | 类型 0:套餐租金 1:话机月租 2:话机最低消费不足 3:套餐最低消费不足 |
| consumptionName | M | int | 消费来源 |
| time | M | long | 时间（UTC 1970-01-01 至今的毫秒 数 ） |

3.65 获取所有账户账号
接口地址/external/server/GetAllCustomers
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| type | O | int | 获取内容方式，不设置与设置 0 相 同 0:获取 accounts 1:获取 infoCustomerBriefs |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| accounts | O | String [] | 账户账号列表 |
| infoCustomerBriefs | O | InfoCustomerBrief[] | 账户简要信息列表 |

InfoCustomerBrief 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户名称 |
| money | M | double | 账户余额 |
| limitMoney | M | double | 透支限额 |

3.66 半直拨预约被叫号码
接口地址/external/server/ReserveCalleeE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callerE164 | M | String | 主叫号码 |
| calleeE164 | M | String | 被叫被叫号码 |
| accessE164 | M | String | 接入号码（流程所在话机号码） |
| accessE164Password | M | String | 接入号码密码（流程所在话机密码） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.67 创建号码群组
接口地址/external/server/CreateLimitE164Group
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 号码群组名称（具备唯一性的可显 标识） |
| memo | O | String | 备注信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.68 修改号码群组
接口地址 /external/server/ModifyLimitE164Group
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 号码群组名称（具备唯一性的可显 标识） |
| memo | O | String | 备注信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.69 删除号码群组
接口地址/external/server/DeleteLimitE164Group
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 号码群组名称（具备唯一性的可显 标识） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.70 查询号码群组
接口地址/external/server/GetLimitE164Group
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| names | O | String[] | 号码群组列表；支持多个，逗号分 隔 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| infoLimitE164Groups | O | infoLimitE164Group[] | 号码群组信息 |

infoLimitE164Group **格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | O | String | 号码群组名称 |
| memo | O | String | 号码群组备注信息 |

3.71 创建号码群组号码
接口地址/external/server/CreateLimitE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| limitE164GroupName | M | String | 号码组名称 |
| infoLimitE164s | M | InfoLimitE164 [] | 号码组号码列表 |

InfoLimitE164  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 号码 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.72 删除号码群组号码
接口地址/external/server/DeleteLimitE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| limitE164GroupName | M | String | 号码组名称 |
| e164s | M | String [] | 号码组号码列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.73 查询号码群组号码
接口地址/external/server/GetLimitE164
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| limitE164GroupName | M | String | 号码群组名称（具备唯一性的可显 标识） |
| e164 | O | String | 号码；支持多个，逗号分隔 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoLimitE164s | O | infoLimitE164[] | 号码群组下的具体信息 |

infoLimitE164 **格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | O | String | 号码 |
| memo | O | String | 备注信息 |

3.74 创建 Ivr 语音
接口地址/external/server/CreateIvrAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| type | M | int | 语音类型 0:公共语音 1:内置语音 2:彩铃语音 3:企业总机语音 4:回拨直拨语音 5:增值业务语音 6:告警语音 7:语音信箱语音 |
| name | M | String | 语音名称 |
| language | O | String | 语言 |
| ivrServiceName | O | String | 所属流程名称 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| id | O | Integer | 语音标识 |

3.75 修改 Ivr 语音
接口地址/external/server/ModifyIvrAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 语音标识 |
| language | O | String | 语言 |
| ivrServiceName | O | String | 所属流程名称 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.76 删除 Ivr 语音
接口地址/external/server/DeleteIvrAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 语音标识 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.77 获取 Ivr 语音
接口地址/external/server/GetIvrAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| type | O | Integer | 语音类型（与 ids 二选其一） 0:公共语音 1:内置语音 2:彩铃语音 3:企业总机语音 4:回拨直拨语音 5:增值业务语音 6:告警语音 7:语音信箱语音 |
| ids | O | int [] | 语音标识列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoIvrAudios | O | InfoIvrAudio [] | 语音信息列表 |

InfoIvrAudio 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 语音标识 |
| type | M | int | 语音类型 0:公共语音 1:内置语音 2:彩铃语音 3:企业总机语音 4:回拨直拨语音 5:增值业务语音 6:告警语音 7:语音信箱语音 |
| name | M | String | 语音名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| language | M | String | 语言 |
| ivrServiceName | M | String | 所属流程名称 |
| size | M | int | 语音存储大小 |
| memo | M | String | 备注 |

3.78 修改 Ivr 语音数据
接口地址/external/server/ModifyIvrAudioData
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 语音标识 |
| data | M | String | wav 文件信息，需将 byte 流转换为 16 进制字符串（如 byte 值 128 对应 字符串 ”80”  byte  值 0  对应字符 串”00”,byte 值 255 对应字符串”FF” 文件格式: PCM_SIGNED  8000.0  Hz,  16  bit, mono, 2 bytes/frame, little-endian |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.79 创建号码变换表
接口地址/external/server/CreateE164Convert
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| mappingGatewayCallerE1 64 | M | String | 对接网关呼入主叫号码 |
| e164 | M | String | 电话号码 |
| routingGatewayCalleeE16 4 | M | String | 落地网关呼出被叫号码 |
| memo | M | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| id | O | Integer | 唯一标识 |

3.80 修改号码变换表
接口地址/external/server/ModifyE164Convert
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 唯一标识 |
| mappingGatewayCallerE1 64 | O | String | 对接网关呼入主叫号码 |
| routingGatewayCalleeE16 4 | O | String | 落地网关呼出被叫号码 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.81 删除号码变换表
接口地址/external/server/DeleteE164Convert
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 唯一标识 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.82 中断通话
接口地址/external/server/DisconnectCurrentCall
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callIds | M | int [] | 呼叫在软交换中的唯一标识列表。 请参考查询当前通返回的 callId |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.83 获取所有在线话机
接口地址/external/server/GetAllPhoneOnline
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| e164s | O | String[] | 所有在线的话机的电话号码 |

3.84 查询电话卡
接口地址/external/server/GetPhoneCard
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| pin | M | String | 卡号 |
| password | O | String | 密码 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoPhoneCard | O | InfoPhoneCard | 电话卡信息 |

InfoPhoneCard 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| money | M | double | 起始时间（UTC 1970-01-01 至今的 毫秒数 ） |
| limitMoney | M | double | 透支限额 |
| bitsOfConfig | M | int | 卡功能类型 1<<1:允许用于开户 1<<2:开户创建在用电话卡 1<<3:开户创建平台话机 1<<4:允许用于充值 1<<5:充值时替换账户费率 1<<6:充值时套餐加入账户订单 1<<7:卡面值充入账户余额 |
| feeRateGroup | M | String | 费率组名称 |
| expireTime | M | long | 过期时间（UTC 1970-01-01 至今的 毫秒数 ） |
| usedTime | O | Long | 已使用时间（UTC 1970-01-01 至今 的毫秒数 ） 不设置:表示未使用 |
| usedAccount | O | String | 已使用账户 |
| agentAccount | M | String | 代理商账户 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| suiteNames | M | String [] | 套餐名称列表 |
| memo | M | String | 备注信息 |

3.85 创建告警
接口地址/external/server/CreateAlarm
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| name | M | String | 告警名称 |
| level |  | int | 告警级别 0:一般 1:次要 2:主要 3:紧急 |
| value | O | Double | 默认值:0x7fffffff（32 位整形） |
| alarmInfo | O | String | 告警信息 |
| startTime | O | Long | 告警发生时间（UTC 1970-01-01 至 今的毫秒数 ） |
| stopTime | O | Long | 告警结束时间（UTC 1970-01-01 至 今的毫秒数 ） |
| upper | O | Double | 阈值上限 取值范围: 0x80000000～0x7fffffff（32 位整形） |
| lower | O | Double | 阈值下限: 0x80000000～0x7fffffff（32 位整形） |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.86 创建地理围栏
接口地址/external/server/CreateIpLimit
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| area | O | String | 地区名称 |
| ip | M | String | 起始 IP 地址（请符合 ipv4 格式。如 1.1.1.1） |
| count | O | int | 从起始 IP 起的 IP 段总数 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.87 删除地理围栏
接口地址/external/server/Delete IpLimit
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| ips | M | String | 删除对应起始 IP 的 IP 段 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.88 获取当前告警
接口地址/external/server/GetAlarmCurrent
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoAlarmCurrents | O | InfoAlarmCurrent | 当前告警列表 |

InfoAlarmCurrent 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| id | M | int | 告警唯一标识 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| type | M | int | 告警类型 20000:落地网关 ASR 20001:落地网关 ACD 20002:落地网关并发下降 20003:CPU 利用率 20004:内存占用率 20005:硬盘 20006:待处理 CDR 20007:账户余额 20009:接收包速率 20010:接收数据流量 20011:发送包速率 20012:发送数据流量 20013:对接网关 ASR 20014:对接网关 ACD 20015:对接网关并发下降 20016:通话时长 20017:数据库 20018:进程终止 20019:备机启用 20020:非法呼叫 20021:时钟偏差 20022:落地网关并发上升 20023:对接网关并发上升 20026:登录 MAC 受限 20027:主机数据库服务 20028:备机数据库服务 |
| level | M | int | 告警级别 0:一般 1:次要 2:主要 3:紧急 |
| name | M | String | 告警名称 |
| startTime | M | long | 告警开始时间 （UTC 1970-01-01 至今的毫秒数） |
| stopTime | O | Long | 告警结束时间 （UTC 1970-01-01 至今的毫秒数） |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| value | M | double | 告警值 |
| upper | O | Double | 告警阈值上限 |
| lower | O | Double | 告警阈值下限 |
| confirmUser | O | String | 告警确认用户 |
| confirmTime | O | Long | 告警确认时间 （UTC 1970-01-01 至今的毫秒数） |
| memo | M | String | 告警备注 |

3.89 IVR 中断通话
接口地址/external/server/DisconnectIvrCall
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callIdentifiers | M | String [] | IVR 的呼叫 ID 列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.90 创建手机地区
接口地址/external/server/CreateMobileArea
当 mobilePrefix 与存在的信息冲突时，系统将使用当前数据覆盖原有数据
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| infoMobileAreas | M | InfoMobileArea [] | 手机地区信息列表 |

InfoMobileArea  格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| mobilePrefix | M | String | 手机前缀（必须为 7 位数字） 样例:1300000 |
| areaCode | M | String | 地区区号 北京区号样例:10 |
| areaName | O | String | 地区名称 |
| memo | O | String | 备注 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.91 删除手机地区
接口地址/external/server/DeleteMobileArea
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| mobilePrefixes | M | String [] | 手机前缀列表 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |

3.92 获取手机地区
接口地址/external/server/GetMobileArea
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| mobilePrefix | O | String | 手机前缀 不设置:获取所有手机地区 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| infoMobileAreas | O | InfoMobileArea [] | 手机地区信息，参见 创建手机地区 |

**4 ****对外请求**
系统对外请求采用 +JSON  方式，可配置对外请求提交的地址以及接口页面的后缀名称
4.1 对外请求配置
步骤 1  /home/kunshi/vos3000/etc/server.conf 中填写推送地址参数
OUT_POST_URL
步骤 2   重新加载配置
vos3000d reload
步骤 3   开启功能
4.2 IVR 请求外部数据控制语音流程
接口页面:PushDtmfInfo
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| flowNo | M | long | 本呼叫唯一标识 |
| callerE164 | M | String | 主叫号码 |
| calleeE164 | M | String | 被叫号码 |
| accessE164 | M | String | 接入号 |
| menuName | M | String | 菜单名称 |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| dtmf | M | String | 客户按键信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码（由外部系统定义，系统根 据返回码执行后续流程，若为收到 返回信息或无指定后续流程则执行 默认流程） |
| exception | O | String | 错误原因 |
| audioNames | O | String [] | 语音参数列表 |

4.3 IVR 请求外部数据控制语音流程2
接口页面:PushDtmfInfos
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| flowNo | M | long | 本呼叫唯一标识 |
| callerE164 | M | String | 主叫号码 |
| calleeE164 | M | String | 被叫号码 |
| accessE164 | M | String | 接入号 |
| infoDtmfs | M | InfoDtmf [] | 菜单按键信息 |

InfoDtmf 格式
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| menuName | M | String | 菜单名称 |
| dtmf | M | String | 客户按键信息 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码（由外部系统定义，系统根 据返回码执行后续流程，若为收到 返回信息或无指定后续流程则执行 默认流程） |
| exception | O | String | 错误原因 |
| audioNames | O | String [] | 语音参数列表 |

4.4 平台话机上下线通知
接口页面:PhoneOnline
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| e164 | M | String | 话机号码 |
| dids | M | String[] | 一机多号列表 |
| online | M | boolean | true:话机上线 false:话机离线 |
| eventTime | M | long | 事件产生时间 （UTC 1970-01-01 至今的毫秒数） |
| localIp | M | String | 服务器本地 IP |
| localPort | M | int | 服务器本地端口 |
| remoteIp | M | String | 远端 IP |
| productId | M | String | 设备名称 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |

4.5 呼叫状态通知
接口页面:CallStateReport
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callId | M | int | 呼叫唯一标识 |
| callState | M | int | 呼叫状态 -1:呼叫初始化(Setup) -2:呼叫接续中(CallProceeding) -3:        呼   叫    接    续   中 (CallProceeding(RTP)) -4:呼叫接续中(Progress) -5:振铃(Alerting) -6:接通(Connet) -7:呼叫初始化(Invite) -8:呼叫接续中(Trying) -9:呼叫接续中(SessionProgress) -10:        呼   叫   接   续   中 (SessionProgress(SDP)) -11:振铃(Ringing) -12:接通(Ok) -13:挂断(Release) -18:呼叫鉴权中，即还未发送至被叫 方。 |
| eventTime | M | long | 事件产生时间 （UTC 1970-01-01 至今的毫秒数） |
| callerE164 | M | String | 主叫号码 |
| calleeE164 | M | String | 被叫号码 |
| callerGatewayId | O | String | 主叫网关名称 |
| calleeGatewayId | O | String | 被叫网关名称 |
| callerIp | M | String | 主叫 IP |
| calleeIp | M | String | 被叫 IP |
| callerLocalIp | M | String | 主叫接入的本地 IP |
| calleeLocalIp | M | String | 被叫发起的本地 IP |
| transactionId | O | String |  |

| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| callIdentifier | M | String | 主叫 SIP 头域 Call-ID |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |

4.6 账户余额变化
仅当账户充值与非话单类扣费触发 接口页面:CustomerMoneyChange
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| account | M | String | 账户号码 |
| money | M | double | 账户当前余额 |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |

4.7 当前告警通知
接口页面:AlarmCurrentReport
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| infoAlarmCurrents | M | InfoAlarmCurrent [] | 当前告警列表，结构定义参见“获 取当前告警” |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |

**5 ****额外选配接口**
5.1 播放语音
接口地址/external/server/PlayAudio
**请求格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| audioes | M | String | 语音文件名称列表（使用逗号分隔 多个文件名称） |
| language | O | String | 默认使用 accessE164 对应语音流程 的语言 |
| callerDisplayNumber | O | String | 主叫去电显示号码 不设置，表示采用系统默认方式 |
| callee | M | String | 被叫号码 |
| accessE164 | M | String | 接入号码（流程所在话机号码） |
| accessE164Password | M | String | 接入号码密码（流程所在话机密码） |
| billingNumber | O | String | 计费号码 |
| billingNumberType | O | Integer | 计费号码类型 0：根据 billingNumber 对应话机所 在账户计费 2：根据 billingNumber 对应绑定号 码所在账户计费 3：根据 billingNumber 对应在用电 话卡所在账户计费 |
| transactionId | O | String | 提交识别码，用于本次请求与后续 状态通知、话单的对应 字符取值范围 A 至 Z ，a 至 z ，0 至 9，以及- 、_ |

**返回格式**
| 参数名称 | 必须 | 类型 | 描述信息 |
| --- | --- | --- | --- |
| retCode | M | int | 返回码 |
| exception | O | String | 错误原因 |
| transactionId | O | String | 与请求相同 与 CallStateReport  的 transactionId 一致 |
| callIdentifier | O | String | 呼叫唯一标识 与 CallStateReport   的 callIdentifier 一致 |
