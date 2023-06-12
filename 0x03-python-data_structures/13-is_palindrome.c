#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the pointer that has the address of the first node
 */

void reverse_list(listint_t **head)
{
	listint_t *current_node = NULL;
	listint_t *next_node = *head;

	while (*head != NULL)
	{
		next_node = (*head)->next;
		(*head)->next = current_node;
		current_node = *head;
		*head = next_node;
	}
	*head = current_node;
}

/**
 * compare_list - checks if two linked list have the same data
 * @head_1: pointer to the first node of a the first list
 * @head_2: pointer to the first node of a the second list
 * Return: 1 if the two lists have the same data, 0 otherwise
 */

int compare_list(listint_t *head_1, listint_t *head_2)
{
	listint_t *ptr_1 = head_1;
	listint_t *ptr_2 = head_2;

	while (ptr_1 != NULL && ptr_2 != NULL)
	{
		if (ptr_1->n == ptr_2->n)
		{
			ptr_1 = ptr_1->next;
			ptr_2 = ptr_2->next;
		}
		else
		{
			return (0);
		}
	}

	if (ptr_1 == NULL && ptr_2 == NULL)
	{
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - determines if a list is palindrome or not
 * @head: pointer to the pointer that has the address of the first node
 * Return: 1 if it's palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *slow_prev = *head;
	listint_t *mid_node = NULL;
	listint_t *list_sec_half = NULL;
	int flag = 1;

	/* can only move only if list has at least two nodes*/
	if (*head != NULL && (*head)->next != NULL)
	{	/* find middle element*/
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			slow_prev = slow;
			slow = slow->next;
		}


		/* middle element for odd list*/
		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}

		list_sec_half = slow;
		slow_prev->next = NULL;

		/*reverse the second half of the list*/
		reverse_list(&list_sec_half);

		/*compare the two halves*/
		flag = compare_list(*head, list_sec_half);

		/*put back the origional linked list*/
		reverse_list(&list_sec_half);

		if (mid_node != NULL)
		{
			slow_prev->next = mid_node;
			mid_node->next = list_sec_half;
		}
		else
		{
			slow_prev->next = list_sec_half;
		}
	}

	return (flag);

}
