const express = require('express')
const app = express()

const requestTime = function (req, res, next) {
    req.requestTime = Date.now()
    next()
}

app.use(requestTime)

var index = 0

app.get('/', (req, res) => {
    index = index + 1
    let responseText = 'Hello World!<br>'
    responseText += `<small> ${index}-th Requested at: ${req.requestTime}</small>`
    console.log(responseText)
    res.send(responseText)
})

app.listen(3000)