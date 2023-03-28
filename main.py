# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    queries = []
    for i in range(n):
        query_input = input().split()
        query = Query(query_input)
        queries.append(query)
    return queries


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for i in contacts:
                if i.number == cur_query.number:
                    contacts.remove(i)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def main():
    queries = read_queries()
    responses = process_queries(queries)
    write_responses(responses)

if __name__ == '__main__':
    main()

