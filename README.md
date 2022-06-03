# Facebook API

> This is a class for Facebook API that you can use to do many things by Facebook Account

* The class is divided into parts

***

## Access Token

* To do anything on Facebook, it is done through an Access Token
* For example, you want to like on a specific post, you must put the post id and access of account
* To get access token use `access_token()`

``` python
from facebook import facebook

api = facebook()
access_token = api.access_token('<Facebook Account Email>', '<Facebook Account Password>')
```

* This function will set android full access token on class to use it later
* If you already have an Access Token account set it in class via `set_access_token()`

``` python
api.set_access_token('<Access Token of Facebook Account>')
```

***

## Graph API

* Here you can use official Facebook Api by one function `graph(method, object, object_id, params)`

* Method -> What is method you want?
  * Do you want to get data? method = get
  * Do you want to post data? method = post
  * Do you want to delete the data you sent? method = delete

* Object -> The target object
  * There are many objects that you can choose from
  * if you want to comment on post or get list of comments, the object will be `comments`
  * You can learn more by official docs here [Graph API Reference](https://developers.facebook.com/docs/graph-api/reference)

* Object ID -> This is the ID of the object you want to play with

* Params -> For additional parameters
  * For example, if you want to write a comment in a specific post, then you want to a parameter to determine the content of the comment `{'message': 'this is a comment bla bla bla'}`

### Examples

* Get reactions list of post `graph('get', 'reactions', object_id)`
* Delete like from post `graph('delete', 'likes', object_id)`
