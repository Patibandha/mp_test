from search_api import get_most_relevent_search, get_top_5_result


if __name__ == '__main__':
    query = "Circular reference found role inference"
    links = get_top_5_result(query)
    print(links)

    for link in links:
        final_result = get_most_relevent_search(link)
        print(
            "For search query {0}\n "
            "for link {1} \n"
            "most relevant answer would be {2}".format(query, link, final_result)
        )
