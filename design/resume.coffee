# Resume data as a coffee script JavaScript object experiment
# Modeled after LinkedIn's data structures

resume =
    summary: '
        Placeholder
    '

    skills: [
        'JavaScript', 'Python', 'jQuery', 'HTML5', 'CSS3', 'Django',
        'Backbone.js', 'Java', 'JSON', 'Git'
    ]

    experience: [
            company-name: 'The Boeing Company'
            company-website: 'http://boeing.com'
            location: 'Bellevue, WA'
            title: 'Software Developer'
            date-from: 'June 2011'
            date-to: 'Present'
            currently-employed: true
            description:  '
                - Currently leading a team of 15 people to create and manage a
                  GitHub-like collaborative coding environment project using
                  Git and GitLab for a growing list of pilot users

                - Analyzed web/thick-client applications for information/
                  computer-security vulnerabilities

                - Designed and developed a programmable Java interface library
                  to an electrical-engineering IBM mainframe application

                - Designed and developed a multi-threaded Java application
                  nterfacing two major manufacturing/production engineering
                  applications, achieved a speedup of 6.5x over legacy system
            '
        ,
            company-name: 'The Boeing Company'
            company-website: 'http://boeing.com'
            location: 'Bellevue, WA'
            title: 'Software Developer'
            date-from: 'June 2011'
            date-to: 'Present'
            currently-employed: false
            description: '
                - Key developer of Ganeti Web Manager, a web-based virtual
                  machine cluster management system
                  (http://code.osuosl.org/projects/ganeti-webmgr)

                - Key developer of Touchscreen, an interactive kiosk display
                  framework (http://code.osuosl.org/projects/touchscreen)
            '
    ]

    education: [
            school-name: 'Oregon State University'
            degree: 'B.S.'
            field: 'Computer Science'
            date-from: 'Sept. 2008'
            date-to: 'June 2011'
            notes: ''
        ,
            school-name: 'Mt. Hood Community College'
            degree: 'A.S.'
            field: 'Computer Science'
            date-from: 'Sept. 2004'
            date-to: 'June 2008'
            notes: ''
    ]
