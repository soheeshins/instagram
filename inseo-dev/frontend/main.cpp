//#include "httplib.h"
//#include "json.hpp"
#include <iostream>

using namespace std;
//using namespace httplib;
//using namespace nlohmann;
/*
void search_user(string search=""){
    Client cli("127.0.0.1:5000");
    string endpoint = "/users/search";

    json body;
    body["search"] = search;

    auto res = cli.Post(endpoint,body.dump(),"application/json");

    if (res && res->status == 200){
        //cout << res->body << endl;
        json response = json::parse(res->body);
        cout << "status" << response["status"] << endl;
        cout << "user" << response["user"] << endl;
        //cout << res->body << endl;
    }
    else
        cout << res.error() << endl;
}

void delete_me(int user_id){
    Client cli("127.0.0.1:5000");

    string endpoint = "/users/" + to_string(user_id);

    auto res = cli.Delete(endpoint);

    if (res && res->status == 200){
        cout << res->body << endl;
    }
    else
        cout << res.error() << endl;
}

int main() {
    //delete_me(7);
    search_user();
    return 0;
}
    */
void login(){
    cout << "로그인 완료" << endl;
}
void sign_up(){
    cout <<"회원가입 완료" << endl;
}
void first_menu(string user_input = ""){
    while(user_input != "로그인" && user_input != "회원가입"){
        cout << "[메인메뉴]" << endl;
        cout << "로그인 / 회원가입" << endl;
        cout << "이용할 서비스를 입력하세요. : ";
        cin >> user_input;
        cout << user_input << endl;
        cout << endl;
    }
    if(user_input == "로그인")
        login();
    else if(user_input == "회원가입")
        sign_up();
}
void logout(){}
void check_me(){}
void update_me(){}
void delete_me(){}
void check_my_posts(){}
void check_my_comments(){}
void upload_post(){}
void post_list(){}
void choose_post(){} 
void write_comment(){}
void search_user(){}
void search_post(){}


int main(){
    first_menu();


    return 0;
}