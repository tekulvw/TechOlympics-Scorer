import web
import sqlite3

urls = (
    '/', 'Scan',
    '/check', 'Check',
    '/submit', 'Submit'
)

app = web.application(urls, globals())
render = web.template.render('html/', base="layout", globals={'sqlite3':sqlite3, 'web':web, 'str':str, 'int':int})

class Scan(object):
    def GET(self):
        return render.score()

class Check(object):
    def GET(self):
        web.seeother("/")

    def POST(self):
        form = web.input(uuid=None)
        user_list = web.ctx.c.execute("SELECT id FROM Student").fetchall()
        print user_list[0]
        print form.uuid
        if int(form.uuid) not in list(user_list[0]):
            return web.seeother("/")
        event_list = web.ctx.c.execute("SELECT id, name from Events").fetchall()
        #print event_list
        user_data = web.ctx.c.execute("SELECT id, name, school_code FROM Student WHERE (id == :uuid)", {'uuid':int(form.uuid)}).fetchone()
        #print user_data
        school_code = int(user_data[2])
        school_name = web.ctx.c.execute("SELECT name FROM School WHERE (id == :school_code)", {'school_code':school_code}).fetchone()[0]
        #print school_name
        return render.check(id=form.uuid, name=user_data[1], school_name=school_name, event_list=event_list)

class Submit(object):
    def GET(self):
        web.seeother("/")

    def POST(self):
        # TODO Save data into db and update scores
        return render.saved()

def my_loadhook():
    web.ctx.conn = sqlite3.connect('db/userinfo.db')
    web.ctx.c = web.ctx.conn.cursor()

if __name__ == '__main__':
    app.add_processor(web.loadhook(my_loadhook))
    app.run()
