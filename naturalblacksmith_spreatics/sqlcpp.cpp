#include <iostream>
#include <jdbc/mysql_driver.h>
#include <jdbc/mysql_connection.h>
#include <jdbc/cppconn/statement.h>
#include <jdbc/cppconn/resultset.h>
using namespace std;

int main() {
    try {
    cout << "[1] 드라이버 생성 중..." << endl;
    sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();

    cout << "[2] 연결 시도 중..." << endl;
    auto conn = unique_ptr<sql::Connection>(
        driver->connect("tcp://database-1.cn6qq680m8yx.ap-northeast-2.rds.amazonaws.com", "your-use", "your-pass"));

    cout << "[3] 연결 성공! 스키마 설정 중..." << endl;
    conn->setSchema("your-database");

    cout << "[4] 쿼리 실행 중..." << endl;
    auto stmt = unique_ptr<sql::Statement>(conn->createStatement());
    auto res = unique_ptr<sql::ResultSet>(stmt->executeQuery("SELECT 1"));

    cout << "[5] 결과: ";
    while (res->next()) {
        cout << res->getInt(1) << endl;
    }

} catch (sql::SQLException& e) {
    cerr << "[ERROR] MySQL 연결 실패: " << e.what() << endl;
}

    return 0;
}






