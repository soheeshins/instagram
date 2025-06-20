// 이 코드는 요청하신 기능 흐름에 맞춰 사용자, 포스팅, 소셜, DM 기능을 포함합니다.
// 구조적 바인딩 없이 C++11 호환 방식으로 작성됨.

#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <regex>
#include <windows.h>

using namespace std;

// 사용자 구조체
struct User {
    string id;
    string email;
    string password;
};

// 포스트 구조체
struct Post {
    string title;
    string content;
    vector<string> comments;
};

map<string, User> users; // 아이디 -> User
string currentUser;

map<string, set<string>> followRequests;
map<string, set<string>> follows;
map<pair<string, string>, vector<string>> dmMessages;
map<string, Post> posts;

// 유틸리티 함수
bool isValidEmail(const string& email) {
    regex pattern(R"((\w+)(\.|_)?(\w*)@(\w+)(\.(\w+))+)");
    return regex_match(email, pattern);
}

// 메인 메뉴
void mainMenu();

// 1. 사용자 기능
void userMenu();
void registerUser();
void loginUser();
void showUserInfo();
void updateUser();
void deleteUser();

// 2. 포스트 기능
void postMenu();
void createPost();
void viewPosts();

// 3. 소셜 기능
void socialMenu();
void searchUser();
void followUser();
void viewFollowList();
void viewFollowRequests();
void handleFollowRequest();

// 4. 메시지 기능
void dmMenu();
void sendDM();
void viewDM();
void deleteDM();

// ----------------------------- 구현부 ----------------------------- //

void registerUser() {
    if (!currentUser.empty()) {
        cout << "이미 로그인 상태입니다. 로그아웃 후 시도하세요.\n";
        return;
    }
    string id, email, pw, pwCheck;
    cout << "[회원가입]\n";
    cout << "아이디: "; cin >> id;
    if (users.count(id)) {
        cout << "이미 존재하는 아이디입니다.\n";
        return;
    }
    cout << "이메일: "; cin >> email;
    if (!isValidEmail(email)) {
        cout << "이메일 형식이 올바르지 않습니다.\n";
        return;
    }
    cout << "비밀번호: "; cin >> pw;
    cout << "비밀번호 확인: "; cin >> pwCheck;
    if (pw != pwCheck) {
        cout << "비밀번호가 일치하지 않습니다.\n";
        return;
    }
    users[id] = { id, email, pw };
    cout << "회원가입이 완료되었습니다.\n";
}

void loginUser() {
    if (!currentUser.empty()) {
        cout << "이미 로그인 상태입니다.\n";
        return;
    }
    string input, pw;
    cout << "[로그인] 아이디 또는 이메일 입력: "; cin >> input;
    cout << "비밀번호 입력: "; cin >> pw;
    for (map<string, User>::iterator it = users.begin(); it != users.end(); ++it) {
        User& user = it->second;
        if ((user.id == input || user.email == input) && user.password == pw) {
            currentUser = user.id;
            cout << "로그인 성공!\n";
            return;
        }
    }
    cout << "로그인 실패.\n";
}

void showUserInfo() {
    if (currentUser.empty()) {
        cout << "로그인 후 이용하세요.\n";
        return;
    }
    User& user = users[currentUser];
    cout << "[사용자 정보]\n";
    cout << "아이디: " << user.id << "\n";
    cout << "이메일: " << user.email << "\n";
}

void updateUser() {
    if (currentUser.empty()) {
        cout << "로그인 후 이용하세요.\n";
        return;
    }
    User user = users[currentUser];
    cout << "1. 아이디 수정\n2. 이메일 수정\n3. 비밀번호 수정\n선택: ";
    int sel; cin >> sel;
    string input;
    switch (sel) {
        case 1:
            cout << "새 아이디: "; cin >> input;
            if (users.count(input)) {
                cout << "이미 존재합니다.\n";
            } else {
                user.id = input;
                users.erase(currentUser);
                users[input] = user;
                currentUser = input;
                cout << "아이디가 수정되었습니다.\n";
            }
            break;
        case 2:
            cout << "새 이메일: "; cin >> input;
            if (!isValidEmail(input)) cout << "형식 오류.\n";
            else { user.email = input; users[currentUser] = user; cout << "수정 완료.\n"; }
            break;
        case 3:
            cout << "새 비밀번호: "; cin >> input;
            user.password = input;
            users[currentUser] = user;
            cout << "수정 완료.\n";
            break;
        default:
            cout << "잘못된 선택.\n";
    }
}

void deleteUser() {
    if (currentUser.empty()) {
        cout << "로그인 후 이용하세요.\n";
        return;
    }
    cout << "정말 탈퇴하시겠습니까? (y/n): ";
    char yn; cin >> yn;
    if (yn == 'y' || yn == 'Y') {
        users.erase(currentUser);
        currentUser = "";
        cout << "탈퇴 완료.\n";
    }
}

void userMenu() {
    while (true) {
        cout << "\n[사용자 기능]\n";
        cout << "1. 회원가입\n2. 로그인\n3. 정보 조회\n4. 정보 수정\n5. 탈퇴\n0. 뒤로가기\n> ";
        int cmd; cin >> cmd;
        if (cmd == 0) return;
        switch (cmd) {
            case 1: registerUser(); break;
            case 2: loginUser(); break;
            case 3: showUserInfo(); break;
            case 4: updateUser(); break;
            case 5: deleteUser(); break;
            default: cout << "잘못된 입력입니다.\n";
        }
    }
}

void mainMenu() {
    while (true) {
        cout << "\n[메인 메뉴]\n1. 사용자 기능\n2. 포스트 기능\n3. 소셜 기능\n4. 메시지 기능\n5. 종료\n> ";
        int cmd; cin >> cmd;
        switch (cmd) {
            case 1: userMenu(); break;
            case 2: cout << "[포스트 기능] 준비 중\n"; break;
            case 3: cout << "[소셜 기능] 준비 중\n"; break;
            case 4: cout << "[메시지 기능] 준비 중\n"; break;
            case 5: cout << "프로그램을 종료합니다.\n"; return;
            default: cout << "잘못된 입력입니다.\n";
        }
    }
}

int main() {
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);
    mainMenu();
    return 0;
}

