
/**加速过程中内核的内部错误
*/
enum EGaccInnerErrorCode
{
    EGACCIEC_OK                     = 0,
 
    /////////////LSP安装/卸载失败错误码////////////////////
    EGACCIEC_LSP_BEGINE             = 1001,
   
    EGACCIEC_LSP_INST_EMPTY_ORI_BUFF  = EGACCIEC_LSP_BEGINE, //originalProtocolInfoBuffer 空
    EGACCIEC_LSP_INST_INST_DUMMY,                           //安装dummy provider失败
    EGACCIEC_LSP_INST_UUID_CREATE,                          // UUID生成失败
    EGACCIEC_LSP_INST_INST_REAL,                            //安装TCP/UDP/RAW provider
    EGACCIEC_LSP_INST_GLOBALALLOC,                          //分配全局堆失败
    EGACCIEC_LSP_INST_WRITEORDER,                           //重写provider order失败
    EGACCIEC_LSP_INST_GETPROVIDER,                          //获取provider列表失败
    EGACCIEC_LSP_INST_REORDER,                              //reorder失败
 
    EGACCIEC_LSP_REG_INST_BACKUP = 1250,                    //reg备份失败
    EGACCIEC_LSP_REG_INST_MEMORY_INST,                      //内存中安装LSP失败
    EGACCIEC_LSP_REG_INST_MEMORY_TO_FILE,                   //从内存中安装到注册表失败
 
    EGACCIEC_LSP_UNINST_DEINST_DUMMY = 1500,                //使用API卸载dummy失败
    EGACCIEC_LSP_UNINST_DEINST_REAL,                        //使用api卸载 TCP/UDP/RAW provider失败
 
    EGACCIEC_LSP_REG_UNINST_DEINST = 1750,               //使用注册表卸载lsp失败
    EGACCIEC_LSP_REG_UNINST_MEMORY,                      //使用注册表从内存中卸载LSP失败
 
    EGACCIEC_LSP_END            = 2000,
 
 
    ///////////////// Local svr 错误码 ////////////////////////
    EGACCIEC_LOCALSVR_BEGINE           = 2001,
 
    EGACCIEC_LOCALSVR_EXCEPTION_GET_TCP_PORT = 2101,     //localsvr启动exception:get tcp port
    EGACCIEC_LOCALSVR_EXCEPTION_GET_UDP_PORT,            //localsvr启动exception:get udp port
    EGACCIEC_LOCALSVR_EXCEPTION_START_TCP_SERVER,        //localsvr启动exception:start tcp svr
    EGACCIEC_LOCALSVR_EXCEPTION_START_UDP_SERVER,        //localsvr启动exception:start udp svr
    EGACCIEC_LOCALSVR_EXCEPTION_OPEN_SHAREDMEM,             //localsvr启动exception:open shared mem
    EGACCIEC_LOCALSVR_EXCEPTION_WRITE_SHAREDMEM,         //localsvr启动exception:write shared mem
    EGACCIEC_LOCALSVR_EXCEPTION_START_PERF_MONITOR,         //localsvr启动exception:start perf monitor
 
    EGACCIEC_LOCALSVR_END                  = 3000,
 
    ///////////////// GetProxySvrInfo 错误码 /////////////////////
    EGACCIEC_GETPROXYSVRINFO_BEGINE        = 3001,
 
    EGACCIEC_GETPROXYSVRINFO_FUNC_CALL = EGACCIEC_GETPROXYSVRINFO_BEGINE, //函数调用错误
 
    EGACCIEC_GETPROXYSVRINFO_NET_DISCONNECTED = 3100,                  //断网
    EGACCIEC_GETPROXYSVRINFO_NET_PARSEFAILURE,                         //回包解析错误
 
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_OTHER = 3200,                     //Aurora, 其他错误
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_CONNECT_FAILED,               //Aurora, 未能连接到服务器
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_SHUTDOWN,                         //Aurora,连接成功，但又被关闭
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_REJECTED,                         //Aurora,服务器拒绝
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_TIMEOUT,                      //Aurora, 超时，有数据传输
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_CANCEL,                       //Aurora,用户取消
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_RESPONSE_FORMAT,                  //Aurora,数据打包格式错误导致无法解析
    EGACCIEC_GETPROXYSVRINFO_RPC_ERR_TIMEOUT_PARITALDATA,              //Aurora, 超时，有数据传输
 
    EGACCIEC_GETPROXYSVRINFO_END           = 4000,
 
    ///////////////// ISP 精测 错误码  ////////////////////////////
    EGACCIEC_ISPPROBE_BEGINE           = 4001,
 
    EGACCIEC_ISPPROBE_FUNC_CALL = EGACCIEC_ISPPROBE_BEGINE,
    EGACCIEC_ISPPROBE_NET_DISCONNECTED = 4100,                         //断网
    EGACCIEC_ISPPROBE_NET_PARSEFAILED,                             //回包解析错误
 
    EGACCIEC_ISPPROBE_RPC_ERR_OTHER = 4200,                            //Aurora, 其他错误
    EGACCIEC_ISPPROBE_RPC_ERR_CONNECT_FAILED,                      //Aurora, 未能连接到服务器
    EGACCIEC_ISPPROBE_RPC_ERR_SHUTDOWN,                                //Aurora,连接成功，但又被关闭
    EGACCIEC_ISPPROBE_RPC_ERR_REJECTED,                                //Aurora,服务器拒绝
    EGACCIEC_ISPPROBE_RPC_ERR_TIMEOUT,                             //Aurora, 超时，有数据传输
    EGACCIEC_ISPPROBE_RPC_ERR_CANCEL,                              //Aurora,用户取消
    EGACCIEC_ISPPROBE_RPC_ERR_RESPONSE_FORMAT,                         //Aurora,数据打包格式错误导致无法解析
    EGACCIEC_ISPPROBE_RPC_ERR_TIMEOUT_PARITALDATA,                     //Aurora, 超时，有数据传输
 
    EGACCIEC_ISPPROBE_END                  = 5000
};
