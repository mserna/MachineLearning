#include "Matrix.h"

using namespace std;

class Matrix {
    
    // Constructor
    Matrix(rows, cols) {
        this->rows = rows;
        this->cols = cols;
        this->data = new Array();

        for(int i = 0; i < this->rows; i++){
            this->data[i] = 0;
            for(int j = 0; j < this->cols; j++){
                this->data[i][j] = [];
            }
        }
    }

    print() {
        for(int i = 0; i < this->rows; i++){
            cout << endl;
            for(int j = 0; j < this->cols; j++){
                cout << this->data[i][j] << end;
            }
        }
    }
}