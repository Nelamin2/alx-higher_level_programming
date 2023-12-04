#include "lists.h"
/**
 * reverse_list - Reverse a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *q = *head;
listint_t *p = *head;
listint_t *second_half;
listint_t *revers;
if (*head == NULL || (*head)->next == NULL)
return (1);
while (p != NULL && p->next != NULL)
{
p = p->next->next;
q = q->next;
}
if (p != NULL)
q = slow->next;
second_half = reverse_list(q);
while (second_half != NULL)
{
if ((*head)->n != second_half->n)
return (0);
*head = (*head)->next;
second_half = second_half->next;
}
return (1);
}
