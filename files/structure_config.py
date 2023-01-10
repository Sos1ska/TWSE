def systemC():
    a = {
    "Start Clear Window":"Yes",
    "Start Show Banner":"Yes",
    "Clear Every Time":"Yes",
    "Record Info in DataBase":"No",
    "Ways":{
        "info":"files\\log\\info.log",
        "error":"files\\log\\error.log",
        "debug":"files\\log\\debug.log",
        "warning":"files\\log\\warn.log",
        "general":"files\\log\\general.log"
    },
    "DataBase":{
        "Way":"files\\database\\",
        "Name":"information.db"
    }
}
    return a

def user():
    a = {
        "NickName":"TWSEUser",
        "ProgramName":"@TWSE",
        "Language":"RUS"
    }

    return a
