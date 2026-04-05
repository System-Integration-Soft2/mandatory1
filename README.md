# System Integration mandatory 1

## ASSIGNMENT DESCRIPTION ##

# Design and develop the following endpoints:

# 1. Books: create, read by ID, list with pagination (limit and offset), update, delete
# 2. Authors: create, read by ID, list all, update, delete
# 3. Publishers: create, read by ID, list all, update, delete


## REST ENDPOINTS NAMING ##

# 1. Books: create, read by ID, list with pagination (limit and offset), update, delete

# POST /books                      # CREATE Books

# GET /books                       # List with pagination (?limit=10&offset=0)

# GET /books/{bookId}              # Read by ID 

# PUT /books/{bookId}              # UPDATE Books

# DELETE /books/{bookId}           # DELETE Books


# 2. Authors: create, read by ID, list all, update, delete

# POST /authors                    # CREATE Author

# GET /authors/{authorId}          # Read by ID 

# GET /authors                     # List all Authors

# PUT /authors/{authorId}          # Update Author

# DELETE /authors/{authorId}       # Delete Author


# 3. Publishers: create, read by ID, list all, update, delete

# POST /publishers                 # CREATE

# GET /publishers/{publisherId}     # Read by ID

# GET /publishers                  # List All publishers

# PUT /publishers/{publisherId}    # UPDATE publisher

# DELETE /publishers/{publisherId} # Delete Publisher

