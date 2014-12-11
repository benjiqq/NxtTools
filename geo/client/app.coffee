###
Nxt Geo client application

TODO:
* show spinner while getting peer data
###


svg = null
projection = null


Meteor.startup ->
    Session.setDefault('peers_loading', true)



Meteor.subscribe 'peers', ->
    console.log "got peers", Peers.find().count()
    Session.setDefault('peers_loading', false)
    makeGraph(svg)


_.extend Template.peers,

    loading: ->
        Session.get("peers_loading")

    peers: ->
        Peers.find()

    numpeers: ->
        Peers.find().count()



makeGraph = (svg) ->

    g2 = svg.append("g") # circles

    apeers = []

    Peers.find({},limit:1000).forEach (peer) ->
        newp = {longitude: peer.longitude, latitude: peer.latitude}
        console.log "newp " + newp
        apeers.push newp
        
    console.log "pc: " + Peers.find().count()
    console.log "pc: " + apeers.length
    console.log "ap: " + apeers[0].longitude

    svgcircles = g2.selectAll('circles').data(apeers).enter().append('circle')

    ca = svgcircles \
        .attr('r', (d) -> 6)  \
        .attr('fill', (d) -> 'blue')

    ca.attr "transform", (d) ->
        console.log(d)
        t = projection([d.longitude, d.latitude])
        console.log("t: " + t)
        "translate(" + t + ")"



_.extend Template.vis,

    ready: ->
        Peers.ready()
        
    created: ->
        Meteor.subscribe 'peers'

    waitOn: ->
        return Meteor.subscribe 'peers'
        
    rendered: ->
            
        place1 = {longitude: 0.2, latitude: 40.3}

        w = 1200;  h = 600



        projection = d3.geo.equirectangular().scale(150).translate([w / 2, h / 2])

        cont = d3.select('#container') 
        svg = cont.append('svg').attr('width', w).attr('height', h)
        
        g1 = svg.append("g") # countries
        
        path = d3.geo.path().projection(projection);

        Meteor.call 'getWorld', (err, result) ->
            world = result.data

            countries = topojson.feature(world, world.objects.countries).features
            
            countries = countries.filter (d) ->
                    return d.id != 10 #'Antarctica'                
                                                                        
            country = g1.selectAll(".country").data(countries);
            country.enter().append("path").attr("d", path).attr('fill','#999')

            makeGraph(svg)


        
