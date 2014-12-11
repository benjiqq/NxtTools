
getPeers = () ->
    # get peers from Nxt 
    bURL = "http://127.0.0.1:7876/nxt?requestType=getPeers"
    w = HTTP.call('GET',bURL).content
    p = JSON.parse(w).peers
    for peer in p
        Peers.insert({'ip': peer})

getGeo = (ip) ->
    # get geoIP from this webservice (could be MaxMind's database locally instead)
    url = "http://www.telize.com/geoip/" + ip
    r = HTTP.call('GET', url)
    result = JSON.parse(r.content)
    #console.log "geo loc" + result
    result

getAll = (peers) ->
    peers.forEach (peer) ->         
        console.log "ip: " + peer.ip
        geo = getGeo(peer.ip)
        Peers.update({_id:peer._id}, {$set:{latitude:geo.latitude}})
        Peers.update({_id:peer._id}, {$set:{longitude:geo.longitude}})

        console.log("peer" + peer.latitude)
        console.log("peer" + peer.longitude)


Meteor.startup ->
    peers = Peers.find({}, limit: 1000)
    c = peers.count()
    
    #getAll(peers)
     
    #console.log "peers: " + c

    #getAll(peers)
         
    #if Peers.find().count() == 0
    #    getPeers()
    #else
    #    Peers.remove({})

Meteor.publish 'peers', -> Peers.find()

Meteor.methods

    "getWorld": ->
        w = HTTP.call('GET', 'http://localhost:3000/world-110m.json')
        return w

    "geoIP":  (ip) ->
        getGeo(ip)
        #ip = "46.19.37.108"


