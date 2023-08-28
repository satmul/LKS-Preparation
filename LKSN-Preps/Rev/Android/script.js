Java.perform(function() {
    let MainActivity = Java.use("com.blackbear.lksnapk.MainActivity");
    MainActivity["checkStatus"].implementation = function (role, x) {
        console.log('checkStatus is called' + ', ' + 'role: ' + role + ', ' + 'x: ' + x);
        let ret = this.checkStatus("admin", x);
        console.log('Role: ' + ret);
        return ret;
    };
});