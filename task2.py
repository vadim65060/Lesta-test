from CircularBufferList import CircularBufferList
from CircularBufferLinkedList import CircularBufferLinkedList

if __name__ == '__main__':
    start_size = 5
    buffer_list = CircularBufferList(start_size)
    buffer_linked_list = CircularBufferLinkedList()

    for i in range(start_size + 1):
        buffer_list.push(i)
        buffer_linked_list.push(i)

    for i in range(start_size + 1):
        item1 = buffer_list.pull()
        item2 = buffer_linked_list.pull()
        if item1 == item2 == i:
            print(item1, "ok")
        else:
            print(item1, item2, "error")

    print("CircularBufferList size", buffer_list.size())
    print("CircularBufferLinkedList size", buffer_linked_list.size())
