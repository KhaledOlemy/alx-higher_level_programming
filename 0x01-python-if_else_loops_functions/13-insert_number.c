#include "lists.h"
/**
 * insert_node - insert node into singly linked list
 * in its order.
 *
 * @head: head of the list.
 * @number: value to put into node in the list.
 *
 * Return: pointer to the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	curr_node = *head;
	if (!curr_node || curr_node->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (curr_node && curr_node->next && curr_node->next->n < number)
	{
		curr_node = curr_node->next;
	}
	new_node->next = curr_node->next;
	curr_node->next = new_node;
	return (new_node);
}
