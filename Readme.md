# Travel-o-Mania Blog

Travel-o-Mania is a dynamic web blog where users can read various posts about travel experiences, tips, and cultural insights. Built with Flask, this blog pulls data from a REST API and serves content dynamically to the end-users.

## Output


https://github.com/sarvesh-2109/Blog-Capstone-P2/assets/113255836/56fce625-ae12-49d4-876e-24dbc128ceac



## Features

- **Dynamic Content Loading:** Posts are fetched from an external API and rendered dynamically.
- **Responsive Design:** Integrated CSS ensures the blog is accessible and aesthetically pleasing on various devices.
- **Individual Post Pages:** Each post can be viewed on its own page, enhancing readability and user engagement.

## Technologies Used

- **Flask:** A micro web framework written in Python.
- **HTML/CSS:** For structuring and styling the website.
- **Bootstrap:** For responsive design.
- **Requests:** To fetch blog posts from the external API.

## Project Structure

```plaintext
/Travel-o-Mania
|-- main.py           # Flask application setup and routes definition
|-- post.py           # Post class handling API data fetching
|-- templates         # Folder for HTML templates
    |-- index.html    # Homepage displaying all posts
    |-- post.html     # Individual post page
    |-- about.html    # About page template
    |-- contact.html  # Contact page template
|-- static            # Folder for static files
    |-- css           # CSS files
    |-- js            # JavaScript files
    |-- assets        # Images and other assets like favicon
```

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sarvesh-2109/Blog-Capstone-P2
   cd Blog-Capstone-P2
   ```

2. **Create a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install flask requests
   ```

4. **Run the Application**

   ```bash
   python main.py
   ```

   Access the web application at: `http://127.0.0.1:5000/`

## Pages

- **Home Page (`/` or `/home`):** Lists all the blog posts.
- **About Page (`/about`):** Information about the blog or author.
- **Contact Page (`/contact`):** Contact form or details.
- **Post Page (`/post/<int:blog_id>`):** Detailed view of each blog post.

