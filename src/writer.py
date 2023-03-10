

# write scores to index.html file
def write_to_index_html_file(scoreboard, games):
    header = '''<!doctype html> <html lang="en"> <head> <meta charset="utf-8" /> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' /> <meta name="viewport" content="width=device-width" /> <title>FOOT </title> <link href="css/bootstrap.css" rel="stylesheet" /> <link href="css/coming-sssoon.css" rel="stylesheet" />    <!--     Fonts     --> <link href="http://netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.css" rel="stylesheet"> <link href='http://fonts.googleapis.com/css?family=Grand+Hotel' rel='stylesheet' type='text/css'> </head> <body style="background-color: black;"> <nav class="navbar navbar-transparent navbar-fixed-top" role="navigation">  <div class="container"> <!-- Brand and toggle get grouped for better mobile display --> <div class="navbar-header"> <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> </div> <!-- Collect the nav links, forms, and other content for toggling --> <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"> <ul class="nav navbar-nav"> <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown"> <img src="images/flags/US.png"/> English(US) <b class="caret"></b> </a> <ul class="dropdown-menu"> <li><a href="#"><img src="images/flags/DE.png"/> Deutsch</a></li> <li><a href="#"><img src="images/flags/GB.png"/> English(UK)</a></li> <li><a href="#"><img src="images/flags/FR.png"/> Français</a></li> <li><a href="#"><img src="images/flags/RO.png"/> Română</a></li> <li><a href="#"><img src="images/flags/IT.png"/> Italiano</a></li> <li class="divider"></li> <li><a href="#"><img src="images/flags/ES.png"/> Español <span class="label label-default">soon</span></a></li> <li><a href="#"><img src="images/flags/BR.png"/> Português <span class="label label-default">soon</span></a></li> <li><a href="#"><img src="images/flags/JP.png"/> 日本語 <span class="label label-default">soon</span></a></li> <li><a href="#"><img src="images/flags/TR.png"/> Türkçe <span class="label label-default">soon</span></a></li> </ul> </li> </ul> <ul class="nav navbar-nav navbar-right"> <li> <a href="#"> <i class="fa fa-facebook-square"></i> Share </a> </li> <li> <a href="#"> <i class="fa fa-twitter"></i> Tweet </a> </li> <li> <a href="#"> <i class="fa fa-envelope-o"></i> Email </a> </li> </ul> </div><!-- /.navbar-collapse --> </div><!-- /.container --> </nav> <article class="wrapper"> <div class="main"> <!--    Change the image source '/images/default.jpg' with your favourite image.     --> <div class="cover black" data-color="black"></div> <!--   You can change the black color for the filter with those colors: blue, green, red, orange       --> <div class="container"> <h1 class="logo"> Scoreboard 2023 </h1> <!--  H1 can have 2 designs: "logo" and "logo cursive"           --> <div class="content"> <h4 class="motto">'''
    body = '<ul style="list-style: none; display: inline;">'

    for ti_gars in scoreboard:
        body += "<li>" + ti_gars[0] + ": " + str(ti_gars[1]) + "</li>" + "\n"

    body += "</ul> </h4>"
    body += '''<h7 class="motto" style="font-size: large;"><ul style="list-style: none; display: inline;">''' + "\n"

    for game in games:
        body += "<li>" + game + "</li>" + "\n"

    body += "</ul></h7>"

    footer = ' <!-- <div class="subscribe"> <h5 class="info-text"> Join the waiting list for the beta. We keep you posted.  </h5> <div class="row"> <div class="col-md-4 col-md-offset-4 col-sm6-6 col-sm-offset-3 "> <form class="form-inline" role="form"> <div class="form-group"> <label class="sr-only" for="exampleInputEmail2">Email address</label> <input type="email" class="form-control transparent" placeholder="Your email here..."> </div> <button type="submit" class="btn btn-danger btn-fill">Notify Me</button> </form> </div> </div> </div> --> </div> </div> <div class="footer"> <!-- <div class="container"> Made with <i class="fa fa-heart heart"></i> by <a href="http://www.creative-tim.com">Creative Tim</a>. Free download <a href="http://www.creative-tim.com/product/coming-sssoon-page">here.</a> </div> --> </div> </div> </article> </body> <script src="js/jquery-1.10.2.js" type="text/javascript"></script> <script src="js/bootstrap.min.js" type="text/javascript"></script> </html>'
    text = header + body + footer
    f = open("index.html", "w")
    f.write(text)
    f.close()


def frais_new_writer(scoreboard, games, fleches):
    header = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>FOOT</title>
<meta charset="utf-8" /> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' /> <meta name="viewport" content="width=device-width" />
	<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>

<section class="main-content">
		<div class="container">
			<h1 style="color: white;text-align: center; font-size: 70px;">Scoreboard</h1>
			<br>
			<br>
	<div class="row">
'''

    body = f'''<div class="col-sm-4"> <div class="leaderboard-card leaderboard-card--first"> <div class="leaderboard-card__top">
                <h3 class="text-center">{scoreboard[0][1]}</h3> 
                </div> <div class="leaderboard-card__body"> <div class="text-center"> <img src="img/user1.jpg" class="circle-img mb-2" alt="User Img">
                <h5 class="mb-0">{scoreboard[0][0]}</h5><small class="text-success"><i class="fa fa-arrow-up"></i>{fleches[0][1]}</small>
                <hr> <div class="d-flex justify-content-between align-items-center"> </div> </div> </div> </div> </div>'''

    body += f'''<div class="col-sm-4">
					<div class="leaderboard-card leaderboard-card--second">
						<div class="leaderboard-card__top">
							<h3 class="text-center">{scoreboard[1][1]}</h3>
						</div>
						<div class="leaderboard-card__body">
							<div class="text-center">
								<img src="img/user2.jpg" class="circle-img mb-2" alt="User Img">
								<h5 class="mb-0">{scoreboard[1][0]}</h5><small class="text-success"><i class="fa fa-arrow-up"></i>{fleches[1][1]}</small>
								<hr>
							</div>
						</div>
					</div>
				</div>'''

    body += f'''<div class="col-sm-4">
					<div class="leaderboard-card leaderboard-card--third">
						<div class="leaderboard-card__top">
							<h3 class="text-center">{scoreboard[2][1]}</h3>
						</div>
						<div class="leaderboard-card__body">
							<div class="text-center">
								<img src="img/user3.jpg" class="circle-img mb-2" alt="User Img">
								<h5 class="mb-0">{scoreboard[2][0]}</h5><small class="text-success"><i class="fa fa-arrow-up"></i>{fleches[2][1]}</small>
								<hr>
							</div>
						</div>
					</div>
				</div>'''

    body += '''
      <table class="table">'''

    for index, ti_gars in enumerate(scoreboard[3:]):
        index += 3 # we already did top 3 
        if ti_gars[0] == 'casper maître fantôme 👻':
            body += f'''
                
                        <tbody>
                            <tr>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <div class="user-info__basic">
                                            <h5 class="mb-0">{ti_gars[0]}</h5>
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <div class="d-flex align-items-baseline">
                                        <h4 class="mr-1">{ti_gars[1]}</h4><small class="text-danger"><i class="fa fa-arrow-down"></i>{fleches[index][1]}</small>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    '''
        else:
            body += f'''
                
                        <tbody>
                            <tr>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <div class="user-info__basic">
                                            <h5 class="mb-0">{ti_gars[0]}</h5>
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <div class="d-flex align-items-baseline">
                                        <h4 class="mr-1">{ti_gars[1]}</h4><small class="text-success"><i class="fa fa-arrow-up"></i>{fleches[index][1]}</small>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    '''

    body += '''
      </table>'''

    body += '<ul style="color: white; list-type: none;">'
    for game in games:
        body += f'<li style="color: white;"><h4> {game} </h4></li>' + "\n"
    body += "</ul>"


    footer = '''
	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>
</html>'''

    text = header + body + footer
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(text)
    # remove one of them...
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(text)
