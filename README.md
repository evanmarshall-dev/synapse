# Synapse

![Synapse README Banner](./static/images/readme-banner.svg)

**Synapse** is a full-stack alumni networking application built for bootcamp students and graduates to connect, share their journeys, and build meaningful professional relationships. Create posts, engage with peers, and grow your network within a supportive community.

## Why Synapse?

Graduating from a bootcamp is just the beginning of your tech journey. Synapse was built to bridge the gap between learning and professional growth by connecting students and alumni within a shared community. Whether you're looking for mentorship, collaboration opportunities, or simply want to share your success story, Synapse provides the platform to make those connections happen.

## Features

### Core Functionality (MVP)

- **User Authentication:** Secure user registration, login, and session management using Django's built-in auth system
- **Post Management:** Full CRUD operations to create, view, edit, and delete posts about your bootcamp journey
- **Profile Information:** Share your program type, graduation year, and LinkedIn profile with the community
- **Commenting System:** Engage with other posts through comments to foster discussions and connections
- **Mobile-First Design:** Responsive layout optimized for all screen sizes with custom CSS
- **User-Specific Data:** Authorization enforcement ensures users can only modify their own content

### User Experience

- Pre-filled edit forms for seamless post updates
- Intuitive navigation with authentication-aware menu
- Clean, modern UI with consistent theming
- Mobile hamburger menu for responsive navigation

## Getting Started

### Live Application

**Deployed App:** [Synapse on Heroku](https://synapse-app-5df8cf6d0ffe.herokuapp.com/)

### Planning Materials

- **Wireframes:** Mobile-first UI designs
- **ERD:** Database schema with User, Post, and Comment models

## Technologies Used

### Backend

- **Python** - Programming language
- **Django** - Web application framework
- **PostgreSQL** - Relational database
- **Gunicorn** - WSGI HTTP server
- **WhiteNoise** - Static file serving

### Frontend

- **Django Templates** - Server-side templating
- **HTML5** - Markup structure
- **CSS3** - Custom styling with responsive design
- **JavaScript** - Client-side interactivity

### Deployment

- **Backend & Frontend:** Heroku
- **Database:** PostgreSQL (Heroku Postgres)

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- Pipenv (Python package manager)
- PostgreSQL database

### Local Development

1. **Fork then Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Synapse.git
   cd Synapse
   ```

2. **Install dependencies**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Create environment variables**

   Create a `.env` file in the root directory:

   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

4. **Set up the database**

   ```bash
   createdb synapse
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the application**

   Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
Synapse/
├── main_app/
│   ├── migrations/       # Database migrations
│   ├── templates/        # App-specific templates
│   │   ├── home.html
│   │   ├── posts/        # Post CRUD templates
│   │   └── registration/ # Auth templates
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Django forms
│   ├── models.py         # Data models (Post, Comment)
│   ├── urls.py           # URL routing
│   └── views.py          # View logic
├── static/
│   ├── css/              # Stylesheets
│   │   └── base.css
│   └── js/               # JavaScript files
│       └── main.js
├── synapse/
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI application
├── templates/
│   └── base.html         # Base template
├── manage.py             # Django management script
├── Pipfile               # Python dependencies
├── Procfile              # Heroku deployment config
└── README.md
```

## Attributions

- **Icons:** System default icons
- **Fonts:** System font stack for optimal performance
- **Framework:** [Django Documentation](https://docs.djangoproject.com/)
- **Deployment Guide:** [Heroku Django Deployment](https://devcenter.heroku.com/articles/deploying-python)

## Next Steps (Planned Enhancements)

### Phase 1: Enhanced UX

- [ ] User profile pages with avatar and bio
- [ ] Search functionality for posts and users
- [ ] Filter posts by program type or graduation year
- [ ] Rich text editor for post content
- [ ] Image upload for posts

### Phase 2: Social Features

- [ ] Follow/unfollow other users
- [ ] Direct messaging between users
- [ ] Notification system for new comments and follows

### Phase 3: Advanced Features

- [ ] AWS S3 integration for media storage
- [ ] Email verification for new users
- [ ] Password reset functionality

## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/evanmarshall-dev">
        <img src="https://github.com/evanmarshall-dev.png" width="100px;" alt="Evan Marshall"/><br />
        <sub><b>Evan Marshall</b></sub>
      </a><br />
      <sub>Contributor</sub>
    </td>
    <td align="center">
      <a href="https://github.com/JAlmonte295">
        <img src="https://github.com/JAlmonte295.png" width="100px;" alt="JAlmonte295"/><br />
        <sub><b>JAlmonte295</b></sub>
      </a><br />
      <sub>Lead Developer</sub>
    </td>
    <td align="center">
      <a href="https://github.com/mrmkmtch">
        <img src="https://github.com/mrmkmtch.png" width="100px;" alt="mrmkmtch"/><br />
        <sub><b>mrmkmtch</b></sub>
      </a><br />
      <sub>Contributor</sub>
    </td>
    <td align="center">
      <a href="https://github.com/TeridkMDupont">
        <img src="https://github.com/TeridkMDupont.png" width="100px;" alt="TeridkMDupont"/><br />
        <sub><b>TeridkMDupont</b></sub>
      </a><br />
      <sub>Contributor</sub>
    </td>
  </tr>
</table>

---

**Built with ❤️ by the Synapse Team**
_Full-Stack Software Engineering Project - 2026_
