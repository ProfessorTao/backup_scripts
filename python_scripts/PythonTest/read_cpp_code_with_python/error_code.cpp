
#include <map>
#include <string>
//#include <>

using namespace std;

#include "error_code.h"

map<int, string> get_error_code(){
    map<int, string> error_code_reason_map;
    string empty_string = "";

    error_code_reason_map[EGACCIEC_OK] = "无错误";
    //error_code_reason_map[EGACCIEC_LSP_BEGINE] = empty_string;

    /////////////LSP安装/卸载失败错误码////////////////////
    error_code_reason_map[EGACCIEC_LSP_INST_EMPTY_ORI_BUFF] = "originalProtocolInfoBuffer 空";
    error_code_reason_map[EGACCIEC_LSP_INST_INST_DUMMY] = "安装dummy provider失败";
    error_code_reason_map[EGACCIEC_LSP_INST_UUID_CREATE] = "UUID生成失败";
    error_code_reason_map[EGACCIEC_LSP_INST_INST_REAL] = "安装TCP/UDP/RAW provider";
    error_code_reason_map[EGACCIEC_LSP_INST_GLOBALALLOC] = "分配全局堆失败";
    error_code_reason_map[EGACCIEC_LSP_INST_WRITEORDER] = "重写provider order失败";
    error_code_reason_map[EGACCIEC_LSP_INST_GETPROVIDER] = "获取provider列表失败";
    error_code_reason_map[EGACCIEC_LSP_INST_REORDER] = "reorder失败";

    return error_code_reason_map;
}
