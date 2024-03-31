from flask import Flask, redirect, url_for, request,render_template,session,send_file
from pytube import YouTube
from os import *
app = Flask(__name__,template_folder="templates")

@app.route('/',methods=["GET"])
def goToHome():
	return redirect("/download")


@app.route("/download",methods=["GET"])
def downloadForm():
	return render_template("index.html")


@app.route("/download",methods=["POST"])
def downloaded():
	link=request.form.get("link")
	youtubeObject = YouTube(link)
	if(request.form.get("value")=="0"):
		youtubeObject = youtubeObject.streams.get_highest_resolution()
	elif(request.form.get("value")=="1"):
		youtubeObject = youtubeObject.streams.get_lowest_resolution()
	else:
		youtubeObject = youtubeObject.streams.get_audio_only()
	try:
		fileName="Download.mp4"
		youtubeObject.download(output_path="Videos",filename=fileName)
	except:
		return "Error Occur During Download"
	relative_filepath = "Videos/Download.mp4"
	absolute_filepath = path.join(getcwd(), relative_filepath)
	return send_file(absolute_filepath,as_attachment=True)
if __name__ == '__main__':
	app.run(debug=True)