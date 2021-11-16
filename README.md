# fake-data-api

An API to create custom fake/dummy data for your application.  
API host: [https://fake-data-api.herokuapp.com](https://fake-data-api.herokuapp.com)

## API Usage

### 1. Get a list of users

`/users/<user-count>`

#### Request Param:

**\<user-count\>** (INT): Represents the number of user data to return

#### Sample JSON Response:

```json
[
  {
    "_id": 1
    "name": {
      "first": "John",
      "last": "Doe",
      "full": "John Doe"
    },
    "gender": "male",
    "contact": {
      "email": "johndoe@email.com",
    }
  }
]
```

<br/>

### 2. Get a fully customized list of data

`/get_fake_data/<data-count>`

#### Request Params:

**\<data-count\>** (INT): Represents the number of custom data to return

> By default there is no index/primary key for each data, so you can add an optional query param at the end of the URL endpoint.  
> e.g. https://fake-data-api.herokuapp.com/get_fake_data/5?include_index=1  
> **include_index** (BOOL): 1 or 0 where 1 means to include data

#### Request Body Params:

|Type Name|Options Name|Options Type|Options Value|
|:---------|:------------|:------------|:-------------|
|first_name|gender (optional)|string|male or female|
|last_name|gender (optional|string|male or female|
|full_name|gender (optional|string|male or female|
|integer|range (required)|array\<int\>|[\<min\>, \<max\>]|
|enum|values (required)|array\<any\>|Unlimited array elements of any type|
|decimal|1. range (required) <br/> 2. decimal_places (required)|1. array\<int\> <br/> 2. int|1. [\<min\>, \<max\>] <br/> 2. Any number of decimal places (e.g. 4)|
|boolean| | | |
|email|gender (optional)|string|male or female|
|image_url|1. category (required) <br/> 2. width (optional)|1. string <br/> 2. int|1. Any category (e.g. nature) <br/> 2. The default width is *1080px* or you can specify the width in px (e.g. 720)|
|words|word_length (required)|int|Number of words you want to include|
|sentence| | | |
|paragraph|paragraph_length (optional) |int|Number of paragraphs you want to include|
|date|range (required)|array\<string\>|[\<from\>,\<to\>] <br/> The string date format is `YYYY-MM-DD`|
|datetime|range (required)|array\<string\>|[\<from\>,\<to\>] <br/> The string datetime format is `YYYY-MM-DD HH:mm:ss`|

#### Sample Body Request:

The JSON body request is written as a data schema like the one shown below.

```json
{
  "first_name": {
    "type": "first_name",
    "options": {
      "gender": "male"
    }
  },
  "last_name": {
    "type": "last_name",
    "options": {
      "gender": "female"
    }
  },
  "full_name": {
    "type": "full_name",
    "options": {
      "gender": "male"
    }
  },
  "age": {
    "type": "integer",
    "options": {
      "range": [18,50]
    }
  },
  "gender": {
    "type": "enum",
    "options": {
      "values": ["male", "female"]
    }
  },
  "rate": {
    "type": "decimal",
    "options": {
      "range": [-50,-10],
      "decimal_places": 4
    }
  },
  "is_member": {
    "type": "boolean"
  },
  "email": {
    "type": "email",
    "options": {
      "gender": "female"
    }
  },
  "image_url": {
    "type": "image_url",
    "options": {
      "category": "nature",
      "width": 500
    }
  },
  "quote": {
    "type": "words",
    "options": {
      "word_length": 5
    }
  },
  "about_me": {
    "type": "sentence"
  },
  "description": {
    "type": "paragraph",
    "options": {
      "paragraph_length": 2
    }
  },
  "date_of_birth": {
    "type": "date",
    "options": {
      "range": ["2021-01-01", "2021-12-31"]
    }
  },
  "created_at": {
    "type": "datetime",
    "options": {
      "range": ["2021-01-01 01:00:00", "2021-12-31 23:00:00"]
    }
  }
}

```

#### Sample JSON Response:

```json
[
  {
    "_id": 0,
    "first_name": "Lori",
    "last_name": "Brown",
    "full_name": "Marie Jimenez",
    "age": 44,
    "gender": "female",
    "rate": -28.0511,
    "is_member": false,
    "email": "helenkammerer8717@email.com",
    "image_url": "https://images.unsplash.com/photo-1439853949127-fa647821eba0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTR8fG5hdHVyZXxlbnwwfHx8fDE2MzcwNzc4OTI&ixlib=rb-1.2.1&q=80&w=500",
    "quote": "quos ipsum ab alias voluptates",
    "about_me": "Vero adipisci omnis cum accusamus vitae qui velit nobis, nostrum minima distinctio, tempora labore dolores doloribus quae magnam nulla voluptate dolor repellendus, impedit architecto voluptates saepe laudantium molestiae ullam velit deserunt placeat, dolore hic dolores.",
    "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "date_of_birth": "2021-11-17",
    "created_at": "2021-09-07 07:49:41"
  }
]

```
