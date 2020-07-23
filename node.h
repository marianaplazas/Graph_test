#ifndef NODE_H
#define NODE_H

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int vertice;
  struct node* next;
} node; 

typedef struct Graph {
  int numVertices;
  int* visitados;

  // We need int** to store a two dimensional array.
  // Similary, we need struct node** to store an array of Linked lists
  struct node** adjLists;
} Graph;
