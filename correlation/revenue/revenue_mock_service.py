import json

mock_data = {
  2018: r'[{"position":23,"rank":23,"name":"Atlanta Hawks","uri":"atlanta-hawks","imageUri":"atlanta-hawks","operatingIncome":22.0,"revenue":209.0,"debtValue":22.0,"oneYearValueChange":30,"valueList":1150,"owners":[{"name":"Tony  Ressler"}]},{"position":5,"rank":5,"name":"Boston Celtics","uri":"boston-celtics","imageUri":"boston-celtics","operatingIncome":85.0,"revenue":257.0,"debtValue":6.0,"oneYearValueChange":14,"valueList":2500,"owners":[{"name":"Wycliffe Grousbeck"},{"name":"Robert Epstein"},{"name":"Irving Grousbeck"},{"name":"Stephen Pagliuca "}]},{"position":6,"rank":6,"name":"Brooklyn Nets","uri":"brooklyn-nets","imageUri":"brooklyn-nets","operatingIncome":52.0,"revenue":273.0,"debtValue":11.0,"oneYearValueChange":28,"valueList":2300,"owners":[{"name":"Mikhail Prokhorov"}]},{"position":28,"rank":28,"name":"Charlotte Hornets","uri":"charlotte-hornets","imageUri":"charlotte-hornets","operatingIncome":21.0,"revenue":202.0,"debtValue":14.0,"oneYearValueChange":35,"valueList":1050,"owners":[{"name":"Michael Jordan"}]},{"position":4,"rank":4,"name":"Chicago Bulls","uri":"chicago-bulls","imageUri":"chicago-bulls","operatingIncome":95.0,"revenue":281.0,"debtValue":3.0,"oneYearValueChange":4,"valueList":2600,"owners":[{"name":"Jerry Reinsdorf"}]},{"position":15,"rank":15,"name":"Cleveland Cavaliers","uri":"cleveland-cavaliers","imageUri":"cleveland-cavaliers","operatingIncome":-6.2,"revenue":280.0,"debtValue":15.0,"oneYearValueChange":10,"valueList":1325,"owners":[{"name":"Dan Gilbert"}]},{"position":9,"rank":9,"name":"Dallas Mavericks","uri":"dallas-mavericks","imageUri":"dallas-mavericks","operatingIncome":21.0,"revenue":233.0,"debtValue":5.0,"oneYearValueChange":31,"valueList":1900,"owners":[{"name":"Mark Cuban"}]},{"position":24,"rank":24,"name":"Denver Nuggets","uri":"denver-nuggets","imageUri":"denver-nuggets","operatingIncome":49.0,"revenue":202.0,"debtValue":0.0,"oneYearValueChange":26,"valueList":1125,"owners":[{"name":" Kroenke Family"}]},{"position":25,"rank":25,"name":"Detroit Pistons","uri":"detroit-pistons","imageUri":"detroit-pistons","operatingIncome":22.0,"revenue":221.0,"debtValue":14.0,"oneYearValueChange":22,"valueList":1100,"owners":[{"name":"Tom Gores"}]},{"position":3,"rank":3,"name":"Golden State Warriors","uri":"golden-state-warriors","imageUri":"golden-state-warriors","operatingIncome":120.0,"revenue":359.0,"debtValue":24.0,"oneYearValueChange":19,"valueList":3100,"owners":[{"name":"Joe Lacob"},{"name":"Peter Guber"}]},{"position":7,"rank":7,"name":"Houston Rockets","uri":"houston-rockets","imageUri":"houston-rockets","operatingIncome":95.0,"revenue":296.0,"debtValue":8.0,"oneYearValueChange":33,"valueList":2200,"owners":[{"name":"Tilman Fertitta"}]},{"position":22,"rank":22,"name":"Indiana Pacers","uri":"indiana-pacers","imageUri":"indiana-pacers","operatingIncome":29.0,"revenue":205.0,"debtValue":11.0,"oneYearValueChange":34,"valueList":1175,"owners":[{"name":"Herbert Simon"},{"name":"Stephen  Simon"}]},{"position":8,"rank":8,"name":"Los Angeles Clippers","uri":"los-angeles-clippers","imageUri":"los-angeles-clippers","operatingIncome":35.0,"revenue":257.0,"debtValue":0.0,"oneYearValueChange":7,"valueList":2150,"owners":[{"name":"Steve Ballmer"}]},{"position":2,"rank":2,"name":"Los Angeles Lakers","uri":"los-angeles-lakers","imageUri":"los-angeles-lakers","operatingIncome":136.0,"revenue":371.0,"debtValue":1.0,"oneYearValueChange":10,"valueList":3300,"owners":[{"name":" Jerry Buss Family Trusts"},{"name":"Philip Anschutz"}]},{"position":29,"rank":29,"name":"Memphis Grizzlies","uri":"memphis-grizzlies","imageUri":"memphis-grizzlies","operatingIncome":15.0,"revenue":206.0,"debtValue":24.0,"oneYearValueChange":30,"valueList":1025,"owners":[{"name":"Robert Pera"}]},{"position":10,"rank":10,"name":"Miami Heat","uri":"miami-heat","imageUri":"miami-heat","operatingIncome":63.0,"revenue":253.0,"debtValue":21.0,"oneYearValueChange":26,"valueList":1700,"owners":[{"name":"Micky Arison"}]},{"position":26,"rank":26,"name":"Milwaukee Bucks","uri":"milwaukee-bucks","imageUri":"milwaukee-bucks","operatingIncome":20.0,"revenue":179.0,"debtValue":40.0,"oneYearValueChange":37,"valueList":1075,"owners":[{"name":"Wes Edens"},{"name":"Jamie Dinan"},{"name":"Marc Lasry"}]},{"position":27,"rank":27,"name":"Minnesota Timberwolves","uri":"minnesota-timberwolves","imageUri":"minnesota-timberwolves","operatingIncome":53.0,"revenue":204.0,"debtValue":13.0,"oneYearValueChange":38,"valueList":1060,"owners":[{"name":"Glen Taylor"}]},{"position":30,"rank":30,"name":"New Orleans Pelicans","uri":"new-orleans-pelicans","imageUri":"new-orleans-pelicans","operatingIncome":37.0,"revenue":204.0,"debtValue":12.0,"oneYearValueChange":33,"valueList":1000,"owners":[{"name":"Tom Benson"}]},{"position":1,"rank":1,"name":"New York Knicks","uri":"new-york-knicks","imageUri":"new-york-knicks","operatingIncome":140.0,"revenue":426.0,"debtValue":1.0,"oneYearValueChange":9,"valueList":3600,"owners":[{"name":" Madison Square Garden Company"}]},{"position":18,"rank":18,"name":"Oklahoma City Thunder","uri":"oklahoma-city-thunder","imageUri":"oklahoma-city-thunder","operatingIncome":64.0,"revenue":222.0,"debtValue":11.0,"oneYearValueChange":22,"valueList":1250,"owners":[{"name":"Clayton Bennett"},{"name":" Aubrey McClendon estate"}]},{"position":19,"rank":19,"name":"Orlando Magic","uri":"orlando-magic","imageUri":"orlando-magic","operatingIncome":39.0,"revenue":211.0,"debtValue":12.0,"oneYearValueChange":33,"valueList":1225,"owners":[{"name":"Richard DeVos"}]},{"position":21,"rank":21,"name":"Philadelphia 76ers","uri":"philadelphia-76ers","imageUri":"philadelphia-76ers","operatingIncome":40.0,"revenue":184.0,"debtValue":13.0,"oneYearValueChange":48,"valueList":1180,"owners":[{"name":"Joshua Harris "},{"name":"David Blitzer"}]},{"position":17,"rank":17,"name":"Phoenix Suns","uri":"phoenix-suns","imageUri":"phoenix-suns","operatingIncome":31.0,"revenue":218.0,"debtValue":14.0,"oneYearValueChange":16,"valueList":1280,"owners":[{"name":"Robert Sarver"}]},{"position":16,"rank":16,"name":"Portland Trail Blazers","uri":"portland-trail-blazers","imageUri":"portland-trail-blazers","operatingIncome":25.0,"revenue":223.0,"debtValue":8.0,"oneYearValueChange":24,"valueList":1300,"owners":[{"name":"Paul Allen"}]},{"position":13,"rank":13,"name":"Sacramento Kings","uri":"sacramento-kings","imageUri":"sacramento-kings","operatingIncome":50.0,"revenue":240.0,"debtValue":38.0,"oneYearValueChange":28,"valueList":1375,"owners":[{"name":"Vivek Ranadive"}]},{"position":11,"rank":11,"name":"San Antonio Spurs","uri":"san-antonio-spurs","imageUri":"san-antonio-spurs","operatingIncome":59.0,"revenue":259.0,"debtValue":5.0,"oneYearValueChange":32,"valueList":1550,"owners":[{"name":"Peter Holt"},{"name":"Julianna Hawn Holt"}]},{"position":12,"rank":12,"name":"Toronto Raptors","uri":"toronto-raptors","imageUri":"toronto-raptors","operatingIncome":51.0,"revenue":250.0,"debtValue":8.0,"oneYearValueChange":24,"valueList":1400,"owners":[{"name":" Bell Canada"},{"name":" Rogers Communications"}]},{"position":20,"rank":20,"name":"Utah Jazz","uri":"utah-jazz","imageUri":"utah-jazz","operatingIncome":61.0,"revenue":221.0,"debtValue":6.0,"oneYearValueChange":32,"valueList":1200,"owners":[{"name":" Miller Family Trust"}]},{"position":14,"rank":14,"name":"Washington Wizards","uri":"washington-wizards","imageUri":"washington-wizards","operatingIncome":21.0,"revenue":222.0,"debtValue":9.0,"oneYearValueChange":35,"valueList":1350,"owners":[{"name":"Ted Leonsis"}]}]',
  2019: r'[{"position":24,"rank":24,"name":"Atlanta Hawks","uri":"atlanta-hawks","imageUri":"atlanta-hawks","operatingIncome":42.0,"revenue":215.0,"debtValue":19.0,"oneYearValueChange":13,"valueList":1300,"owners":[{"name":"Tony  Ressler"}]},{"position":5,"rank":5,"name":"Boston Celtics","uri":"boston-celtics","imageUri":"boston-celtics","operatingIncome":100.0,"revenue":287.0,"debtValue":6.0,"oneYearValueChange":12,"valueList":2800,"owners":[{"name":"Wycliffe Grousbeck"},{"name":"Robert Epstein"},{"name":"Irving Grousbeck"},{"name":"Stephen Pagliuca "}]},{"position":6,"rank":6,"name":"Brooklyn Nets","uri":"brooklyn-nets","imageUri":"brooklyn-nets","operatingIncome":53.0,"revenue":290.0,"debtValue":9.0,"oneYearValueChange":2,"valueList":2350,"owners":[{"name":"Mikhail Prokhorov"},{"name":"Joseph Tsai"}]},{"position":28,"rank":28,"name":"Charlotte Hornets","uri":"charlotte-hornets","imageUri":"charlotte-hornets","operatingIncome":22.0,"revenue":213.0,"debtValue":12.0,"oneYearValueChange":19,"valueList":1250,"owners":[{"name":"Michael Jordan"}]},{"position":4,"rank":4,"name":"Chicago Bulls","uri":"chicago-bulls","imageUri":"chicago-bulls","operatingIncome":114.0,"revenue":287.0,"debtValue":3.0,"oneYearValueChange":12,"valueList":2900,"owners":[{"name":"Jerry Reinsdorf"}]},{"position":25,"rank":25,"name":"Cleveland Cavaliers","uri":"cleveland-cavaliers","imageUri":"cleveland-cavaliers","operatingIncome":-13.0,"revenue":302.0,"debtValue":16.0,"oneYearValueChange":-4,"valueList":1275,"owners":[{"name":"Dan Gilbert"}]},{"position":8,"rank":8,"name":"Dallas Mavericks","uri":"dallas-mavericks","imageUri":"dallas-mavericks","operatingIncome":99.0,"revenue":287.0,"debtValue":10.0,"oneYearValueChange":18,"valueList":2250,"owners":[{"name":"Mark Cuban"}]},{"position":21,"rank":21,"name":"Denver Nuggets","uri":"denver-nuggets","imageUri":"denver-nuggets","operatingIncome":47.0,"revenue":222.0,"debtValue":0.0,"oneYearValueChange":22,"valueList":1375,"owners":[{"name":" Kroenke Family"}]},{"position":26,"rank":26,"name":"Detroit Pistons","uri":"detroit-pistons","imageUri":"detroit-pistons","operatingIncome":52.0,"revenue":235.0,"debtValue":12.0,"oneYearValueChange":15,"valueList":1270,"owners":[{"name":"Tom Gores"}]},{"position":3,"rank":3,"name":"Golden State Warriors","uri":"golden-state-warriors","imageUri":"golden-state-warriors","operatingIncome":103.0,"revenue":401.0,"debtValue":23.0,"oneYearValueChange":13,"valueList":3500,"owners":[{"name":"Joe Lacob"},{"name":"Peter Guber"}]},{"position":7,"rank":7,"name":"Houston Rockets","uri":"houston-rockets","imageUri":"houston-rockets","operatingIncome":103.0,"revenue":326.0,"debtValue":8.0,"oneYearValueChange":5,"valueList":2300,"owners":[{"name":"Tilman Fertitta"}]},{"position":20,"rank":20,"name":"Indiana Pacers","uri":"indiana-pacers","imageUri":"indiana-pacers","operatingIncome":50.0,"revenue":222.0,"debtValue":9.0,"oneYearValueChange":19,"valueList":1400,"owners":[{"name":"Herbert Simon"},{"name":"Stephen  Simon"}]},{"position":9,"rank":9,"name":"Los Angeles Clippers","uri":"los-angeles-clippers","imageUri":"los-angeles-clippers","operatingIncome":40.0,"revenue":258.0,"debtValue":0.0,"oneYearValueChange":2,"valueList":2200,"owners":[{"name":"Steve Ballmer"}]},{"position":2,"rank":2,"name":"Los Angeles Lakers","uri":"los-angeles-lakers","imageUri":"los-angeles-lakers","operatingIncome":147.0,"revenue":395.0,"debtValue":1.0,"oneYearValueChange":12,"valueList":3700,"owners":[{"name":" Jerry Buss Family Trusts"},{"name":"Philip Anschutz"}]},{"position":30,"rank":30,"name":"Memphis Grizzlies","uri":"memphis-grizzlies","imageUri":"memphis-grizzlies","operatingIncome":27.0,"revenue":213.0,"debtValue":27.0,"oneYearValueChange":17,"valueList":1200,"owners":[{"name":"Robert Pera"}]},{"position":10,"rank":10,"name":"Miami Heat","uri":"miami-heat","imageUri":"miami-heat","operatingIncome":40.0,"revenue":259.0,"debtValue":23.0,"oneYearValueChange":3,"valueList":1750,"owners":[{"name":"Micky Arison"}]},{"position":22,"rank":22,"name":"Milwaukee Bucks","uri":"milwaukee-bucks","imageUri":"milwaukee-bucks","operatingIncome":25.0,"revenue":204.0,"debtValue":31.0,"oneYearValueChange":26,"valueList":1350,"owners":[{"name":"Wes Edens"},{"name":"Jamie Dinan"},{"name":"Marc Lasry"}]},{"position":27,"rank":27,"name":"Minnesota Timberwolves","uri":"minnesota-timberwolves","imageUri":"minnesota-timberwolves","operatingIncome":47.0,"revenue":223.0,"debtValue":12.0,"oneYearValueChange":19,"valueList":1260,"owners":[{"name":"Glen Taylor"}]},{"position":29,"rank":29,"name":"New Orleans Pelicans","uri":"new-orleans-pelicans","imageUri":"new-orleans-pelicans","operatingIncome":29.0,"revenue":214.0,"debtValue":14.0,"oneYearValueChange":22,"valueList":1220,"owners":[{"name":"Gayle Benson"}]},{"position":1,"rank":1,"name":"New York Knicks","uri":"new-york-knicks","imageUri":"new-york-knicks","operatingIncome":155.0,"revenue":443.0,"debtValue":1.0,"oneYearValueChange":11,"valueList":4000,"owners":[{"name":" Madison Square Garden Company"}]},{"position":18,"rank":18,"name":"Oklahoma City Thunder","uri":"oklahoma-city-thunder","imageUri":"oklahoma-city-thunder","operatingIncome":10.0,"revenue":241.0,"debtValue":9.0,"oneYearValueChange":18,"valueList":1475,"owners":[{"name":"Clayton Bennett"},{"name":" Aubrey McClendon estate"}]},{"position":23,"rank":23,"name":"Orlando Magic","uri":"orlando-magic","imageUri":"orlando-magic","operatingIncome":64.0,"revenue":223.0,"debtValue":11.0,"oneYearValueChange":8,"valueList":1325,"owners":[{"name":" DeVos family"}]},{"position":12,"rank":12,"name":"Philadelphia 76ers","uri":"philadelphia-76ers","imageUri":"philadelphia-76ers","operatingIncome":68.0,"revenue":268.0,"debtValue":6.0,"oneYearValueChange":40,"valueList":1650,"owners":[{"name":"Joshua Harris"},{"name":"David Blitzer"}]},{"position":17,"rank":17,"name":"Phoenix Suns","uri":"phoenix-suns","imageUri":"phoenix-suns","operatingIncome":47.0,"revenue":235.0,"debtValue":12.0,"oneYearValueChange":17,"valueList":1500,"owners":[{"name":"Robert Sarver"}]},{"position":14,"rank":14,"name":"Portland Trail Blazers","uri":"portland-trail-blazers","imageUri":"portland-trail-blazers","operatingIncome":40.0,"revenue":246.0,"debtValue":8.0,"oneYearValueChange":23,"valueList":1600,"owners":[{"name":" Paul Allen estate"}]},{"position":15,"rank":15,"name":"Sacramento Kings","uri":"sacramento-kings","imageUri":"sacramento-kings","operatingIncome":72.0,"revenue":263.0,"debtValue":34.0,"oneYearValueChange":15,"valueList":1575,"owners":[{"name":"Vivek Ranadive"}]},{"position":13,"rank":13,"name":"San Antonio Spurs","uri":"san-antonio-spurs","imageUri":"san-antonio-spurs","operatingIncome":63.0,"revenue":262.0,"debtValue":6.0,"oneYearValueChange":5,"valueList":1625,"owners":[{"name":"Julianna Hawn Holt"}]},{"position":11,"rank":11,"name":"Toronto Raptors","uri":"toronto-raptors","imageUri":"toronto-raptors","operatingIncome":76.0,"revenue":275.0,"debtValue":7.0,"oneYearValueChange":20,"valueList":1675,"owners":[{"name":" Bell Canada"},{"name":" Rogers Communications"}]},{"position":19,"rank":19,"name":"Utah Jazz","uri":"utah-jazz","imageUri":"utah-jazz","operatingIncome":59.0,"revenue":243.0,"debtValue":7.0,"oneYearValueChange":19,"valueList":1425,"owners":[{"name":" Miller Family Trust"}]},{"position":16,"rank":16,"name":"Washington Wizards","uri":"washington-wizards","imageUri":"washington-wizards","operatingIncome":34.0,"revenue":255.0,"debtValue":8.0,"oneYearValueChange":15,"valueList":1550,"owners":[{"name":"Ted Leonsis"}]}]'
}
def retrieve(year):
  if year in mock_data:
    return mock_data[year]
  else:
    return -1