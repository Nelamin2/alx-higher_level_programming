#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head of the list
 * @number: value to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;
    if (*head == NULL)
    {
        *head = new;
        return new;
    }
    current = *head;
    prev = NULL;
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    if (prev == NULL)
    {
         new->next = *head;
        *head = new;
    }
    else
    {
       prev->next = new;
        new->next = current;
    }
    return new;
}
