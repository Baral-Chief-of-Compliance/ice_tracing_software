export function format_date(date){
    var d = new Date(date)

    var dd = d.getDate()
    if (dd < 10) dd = '0' + dd

    var mm = d.getMonth() + 1
    if (mm < 10) mm = '0' + mm

    var yy = d.getFullYear()

    return dd + '.' + mm + '.' + yy
}