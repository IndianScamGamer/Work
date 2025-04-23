#include <stdio.h>

void removeSecondNode(Node *head){
    Node *current = head;
    while(current && current->next){
        Node *remove = current->next;
        current->next = remove->next;
        free(remove);
        current = current->next;
    }
}
void removeEveryThirdNode(Node *head) {
    Node *current = head;
    while (current && current->next && current->next->next) {
        Node *remove = current->next->next;
        current->next->next = remove->next;
        free(remove);
        current = current->next;
    }
}


void removeDuplicatesSorted(Node *head) {
    Node *current = head;
    while (current && current->next) {
        if (current->value == current->next->value) {
            Node *duplicate = current->next;
            current->next = duplicate->next;
            free(duplicate);
        } else {
            current = current->next;
        }
    }
}