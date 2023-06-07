#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer that contains address of the first node
 * @number: number to be inserted
 * Return: address to new node if successful, otherwose NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;

		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
