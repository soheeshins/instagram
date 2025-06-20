#include <iostream>
#include <string>
#include <map>
#include <windows.h>

using namespace std;

// 사용자 DB (아이디 -> 비밀번호)
map<string, string> users;

// 로그인된 사용자
string currentUser;

// ---------------- 로그인 및 회원가입 ----------------
void registerUser() {
    string id, pw;
    cout << "[회원가입]" << endl;
    cout << "아이디: ";
    cin >> id;
    if (users.count(id)) {
        cout << "이미 존재하는 아이디입니다." << endl;
        return;
    }
    cout << "비밀번호: ";
    cin >> pw;
    users[id] = pw;
    cout << "회원가입이 완료되었습니다." << endl;
}

void login() {
    if (!currentUser.empty()) {
        cout << "이미 로그인되어 있습니다. (" << currentUser << ")" << endl;
        return;
    }

    string id, pw;
    cout << "[로그인]" << endl;
    cout << "아이디: ";
    cin >> id;
    cout << "비밀번호: ";
    cin >> pw;

    if (users.count(id) && users[id] == pw) {
        currentUser = id;
        cout << "로그인 성공! " << currentUser << "님." << endl;
    } else {
        cout << "아이디 또는 비밀번호가 일치하지 않습니다." << endl;
    }
}

// ---------------- 사용자 메뉴 ----------------
void userSelfMenu() {
    while (true) {
        cout << "\n[내 정보 메뉴]" << endl;
        cout << "1. 내 정보 보기" << endl;
        cout << "2. 회원 탈퇴" << endl;
        cout << "3. 뒤로가기" << endl;

        int input;
        cin >> input;
        switch (input) {
            case 1:
                cout << "현재 로그인된 사용자: " << currentUser << endl;
                break;
            case 2:
                cout << "정말 탈퇴하시겠습니까? (y/n): ";
                char yn;
                cin >> yn;
                if (yn == 'y' || yn == 'Y') {
                    users.erase(currentUser);
                    cout << currentUser << "님이 탈퇴되었습니다." << endl;
                    currentUser = "";
                    return;
                }
                break;
            case 3:
                return;
            default:
                cout << "잘못된 입력입니다." << endl;
        }
    }
}

void userOthersMenu() {
    cout << "\n[다른 사용자 목록]" << endl;
    for (const auto& pair : users) {
        if (pair.first != currentUser)
            cout << "- " << pair.first << endl;
    }
}

// ---------------- 사용자 메뉴 ----------------
void userMenu() {
    if (currentUser.empty()) {
        cout << "로그인 후 이용 가능한 메뉴입니다." << endl;
        return;
    }

    while (true) {
        cout << "\n[사용자 메뉴]" << endl;
        cout << "1. 본인" << endl;
        cout << "2. 다른 유저" << endl;
        cout << "3. 뒤로가기" << endl;

        int input;
        cin >> input;
        switch (input) {
            case 1:
                userSelfMenu();
                break;
            case 2:
                userOthersMenu();
                break;
            case 3:
                return;
            default:
                cout << "잘못된 입력입니다." << endl;
        }
    }
}

// ---------------- 메인 메뉴 ----------------
void mainMenu() {
    while (true) {
        cout << "\n[메인 메뉴]" << endl;
        cout << "1. 로그인" << endl;
        cout << "2. 회원가입" << endl;
        cout << "3. 사용자" << endl;
        cout << "4. 종료" << endl;

        int input;
        cin >> input;
        switch (input) {
            case 1:
                login();
                break;
            case 2:
                registerUser();
                break;
            case 3:
                userMenu();
                break;
            case 4:
                cout << "프로그램을 종료합니다." << endl;
                return;
            default:
                cout << "잘못된 입력입니다." << endl;
        }
    }
}

int main() {
    SetConsoleOutputCP(65001); // 출력 콘솔 UTF-8 설정
    SetConsoleCP(65001);       // 입력 콘솔 UTF-8 설정

    mainMenu();
    return 0;
}
