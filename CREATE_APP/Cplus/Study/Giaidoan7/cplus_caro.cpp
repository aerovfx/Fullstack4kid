#include <iostream>
#include <vector>
using namespace std;

// Kích thước bàn cờ
const int n = 3;

// Khởi tạo bàn cờ
std::__1::vector<char> board(n, vector<char>(n, '.'));

void printBoard() {
    // In bàn cờ
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Kiểm tra hàng, cột, hoặc đường chéo có cùng ký tự
bool checkWin(int row, int col, char player) {
    // Kiểm tra hàng
    bool win = true;
    for (int i = 0; i < n; ++i) {
        if (board[row][i] != player) {
            win = false;
            break;
        }
    }
    if (win) return true;

    // Kiểm tra cột
    win = true;
    for (int i = 0; i < n; ++i) {
        if (board[i][col] != player) {
            win = false;
            break;
        }
    }
    if (win) return true;

    // Kiểm tra đường chéo chính
    if (row == col) {
        win = true;
        for (int i = 0; i < n; ++i) {
            if (board[i][i] != player) {
                win = false;
                break;
            }
        }
        if (win) return true;
    }

    // Kiểm tra đường chéo phụ
    if (row + col == n - 1) {
        win = true;
        for (int i = 0; i < n; ++i) {
            if (board[i][n - i - 1] != player) {
                win = false;
                break;
            }
        }
        if (win) return true;
    }

    return false;
}

bool isBoardFull() {
    // Kiểm tra nếu bàn cờ đã đầy
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

void playGame() {
    int row, col;
    char currentPlayer = 'X';

    while (true) {
        printBoard();
        cout << "Lượt của người chơi " << currentPlayer << ". Nhập hàng và cột (0-" << n - 1 << "): ";
        cin >> row >> col;

        // Kiểm tra vị trí hợp lệ
        if (row < 0 || row >= n || col < 0 || col >= n || board[row][col] != '.') {
            cout << "Vị trí không hợp lệ. Hãy chọn lại!" << endl;
            continue;
        }

        // Đánh dấu vị trí
        board[row][col] = currentPlayer;

        // Kiểm tra thắng
        if (checkWin(row, col, currentPlayer)) {
            printBoard();
            cout << "Người chơi " << currentPlayer << " thắng!" << endl;
            break;
        }

        // Kiểm tra hòa
        if (isBoardFull()) {
            printBoard();
            cout << "Trò chơi hòa!" << endl;
            break;
        }

        // Chuyển lượt
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
}

int main() {
    cout << "Chào mừng đến với trò chơi Cờ Caro!" << endl;
    playGame();
    return 0;
}