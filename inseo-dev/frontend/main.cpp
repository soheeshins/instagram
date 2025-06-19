#include "httplib.h"
#include <iostream>

using namespace std;

void search_user(){
    httplib::Client cli("127.0.0.1:5000");
    string endpoint = "/users";
    auto res = cli.Get(endpoint);

    if (res && res->status == 200){
        cout << res->body << endl;
    }
    else
        cout << res.error() << endl;
}

void delete_user(int user_id){
    httplib::Client cli("127.0.0.1:5000");

    string endpoint = "/users/" + to_string(user_id);

    auto res = cli.Delete(endpoint);

    if (res && res->status == 200){
        cout << res->body << endl;
    }
    else
        cout << res.error() << endl;
}

int main() {
    delete_user(7);
    search_user();
    return 0;
}