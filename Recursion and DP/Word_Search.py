def word_search(arr,index_x,index_y,max_x,max_y,match,curr):
    if curr == match:
        return True 
    if index_x > max_x and index_y > max_y:
        return False 
    if index_x > max_x : 
        search_y = word_search(arr,index_x,index_y+1,max_x,max_y,match,curr + arr[index_x][index_y])
    if index_y > max_y:
        search_x = word_search(arr,index_x+1,index_y,max_x,max_y,match,curr + arr[index_x][index_y])
    
    search_x = word_search(arr,index_x+1,index_y,max_x,max_y,match,curr + arr[index_x][index_y])
    search_y = word_search(arr,index_x,index_y+1,max_x,max_y,match,curr + arr[index_x][index_y])
    return search_x or search_y


