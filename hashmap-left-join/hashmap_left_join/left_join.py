from .hashtable import Hashtables


def left_join(table1, table2):
    output = []
    for item in table1.map:
        if item:
            item_value = item.head.value
            if table2.contains(item_value[0]):
                output.append([item_value[0],item_value[1],table2.find(item_value[0])])
            else:
                output.append([item_value[0],item_value[1],None])
    return output

if __name__ == '__main__':
    hashtable1 = Hashtables(1024)
    hashtable1.add('fond', 'enamored')
    hashtable1.add('wrath', 'anger')
    hashtable1.add('diligent', 'employed')
    hashtable1.add('outfit', 'garb')
    hashtable1.add('guide', 'usher')

    hashtable2 = Hashtables(1024)
    hashtable2.add('fond', 'averse')
    hashtable2.add('wrath', 'delight')
    hashtable2.add('diligent', 'idle')
    hashtable2.add('guide', 'follow')
    hashtable2.add('flow', 'jam')

    print(left_join(hashtable1, hashtable2))

