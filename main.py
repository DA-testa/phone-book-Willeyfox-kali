# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Contacts:
    def __init__(self, name):
        self.name = name
        
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
    contacts = []
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = Contact(query.name)
        elif query.type == 'del':
            if query.number in contacts:
                del contacts[query.number]
        else:
            response = contacts.get(query.number)
            if response:
                result.append(response.name)
            else:
                result.append('not found')
    return result

def main():
    queries = read_queries()
    responses = process_queries(queries)
    write_responses(responses)

if __name__ == '__main__':
    main()

