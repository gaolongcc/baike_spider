#-*-coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)



    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            #ascii
            fout.write("<td>%s</td>"% data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['movie_name'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['address'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()

    def output_text(self):

        f = open("download.txt", "a")
        for data in self.datas:
            f.write("%s:%s\n\n" % (data['moive_name'].encode('utf-8'), data['address'].encode('utf-8')))
        f.close()