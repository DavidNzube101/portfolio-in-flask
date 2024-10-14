from flask import Flask, render_template, request

import deviceDetect as dv

app = Flask(__name__)

skills = {
	"HTML": ["None", 95],
	"CSS": ["None", 90],
	"PHP": ['Laravel', 80],
	"Python": ['Flask, Django', 90],
	"JavaScript": ['NodeJS, Angluar', 70],
	"Ruby": ["None", 80],
	"Web Hosting & Deployment": ['Vercel, Hostinger, Netlify, Render, AWS', 100],
	"Database": ['MySQL, VertexxDB, SQlite3, Postgres, Mongo', 92],
	"Team Work": ["None", 97],
	"Adaptability": ['None', 95],
	'Quick Learning': ['None', 96]
}

projects = {
	"Vidbuy": ['vidbuy.png', 'Online marketplace which connects buyers and sellers globally', 'https://www.github.com/DavidNzube101/vidbuy'],
	"Poel": ['Poel_Wide.PNG', 'A really helpful tool for Python-Flask Developer. It automatically creates/generates the files needed for a Standard Flask App.', 'https://www.github.com/DavidNzube101/Poel'],
	"VertexxDB": ['vertexxdb.png', 'A remote based JSON oriented database management system. VertexxDB uses SecJSON to secure data.', 'https://www.github.com/DavidNzube101/VertexxDB'],
	"WRLD": ['WRLD.png', 'A static web development tool that web developers to quickly create, manage, test and maintain static websites.', 'https://www.github.com/DavidNzube101/WRLD'],
	"PaperShare": ['Ps.png', 'A Learning Management Tool that allows teachers to give out homeworks/assignments to students, view them, record them and see insights.', 'https://www.github.com/DavidNzube101/PaperShare']

}

@app.route('/')
def home():

	return render_template('index.html', Skills=skills, Projects=projects)

@app.route('/i')
def homeDkp():

	
	return render_template('index.html', Skills=skills)


@app.route('/more-projects')
def showMoreProjects():
	

	return render_template('projects.html', Projects=projects, _len=len)

if __name__ == "__main__":
	# app.run(debug=True)

	app.run()