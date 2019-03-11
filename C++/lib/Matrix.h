#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <array>

class Matrix {
    public:
    Matrix(int rows, int cols); // Contructor
    // transpose(m);
    // multiply(mat1, mat2);
    // add(mat1, mat2);
    // subtract(mat1, mat2);
    // map(some_func); // Use function for every element in Matrix
    // randomize(); // Initialize matrix with random values
    // ~Matrix(); // Destructor
    void print(); // Prints matrix (mainly for testing)
};

#endif