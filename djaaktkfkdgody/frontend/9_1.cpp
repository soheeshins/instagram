// #include "httplib.h"
// #include <iostream>

// using namespace std;
// using namespace httplib;

// int main() {
//     Client cli("127.0.0.1:5000");

//     string body = R"({
//     "nickname" : "kevin",
//     "password" : "1234",
//     "name" : "이승학"
//     })";

//     auto res = cli.Post("/users", body, "application/json");

//     if (res)
//         cout << res->body << endl;
//     else
//         cout << res.error() << endl;

//     return 0;
    
// }

#include "httplib.h"
#include <iostream>

using namespace std;
using namespace httplib;

int main() {
    Client cli("127.0.0.1:5000");

    // 1. POST: 사용자 생성
    string body = R"({
        "nickname" : "kevin",
        "password" : "1234",
        "name" : "이승학"
    })";

    auto res_post = cli.Post("/users", body, "application/json");
    if (res_post)
        cout << "[POST] 응답: " << res_post->body << endl;
    else
        cout << "[POST] 오류: " << static_cast<int>(res_post.error()) << endl;

    // 2. GET: 사용자 조회
    int user_id = 1;
    string get_endpoint = "/users/" + to_string(user_id);
    auto res_get = cli.Get(get_endpoint);

    if (res_get && res_get->status == 200)
        cout << "[GET] 사용자 정보: " << res_get->body << endl;
    else
        cout << "[GET] 오류 또는 사용자 없음" << endl;

    // 3. DELETE: 사용자 삭제
    string del_endpoint = "/users/" + to_string(user_id);
    auto res_del = cli.Delete(del_endpoint);

    if (res_del && res_del->status == 200)
        cout << "[DELETE] 사용자 삭제됨: " << res_del->body << endl;
    else
        cout << "[DELETE] 삭제 실패" << endl;

    return 0;
}




// #include "httplib.h"

// using namespace httplib;
// using namespace std;

// int main() {
//     Client cli("127.0.0.1:5000")
//     auto res = cli.Get("/");

//     if (res && res->status == 200) {
//         cout << res->body << endl;
//     }
// }

// int user_id = 1;
// string endpoint = "/users/" + to_string(user_id);
// auto res = cli.Get(endpoint);


// int user_id = 1;
// string endpoint = "/users/" + to_string(user_id);
// auto res = cli.Delete(endpoint);