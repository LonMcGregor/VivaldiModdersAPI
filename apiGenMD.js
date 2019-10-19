function generateVivaldiAPI(){
    let vapi = '';
    Object.keys(vivaldi).forEach(api => {
        Object.keys(vivaldi[api]).forEach(method => {
            if(method.indexOf('on')===0){
                vapi += `### [Listener] vivaldi.${api}.${method}\n`;
                vapi += '\n';
            } else if (method.substr(0,1).match('[A-Z]')){
                vapi += `### [Enum] vivaldi.${api}.${method}\n`;
                vapi += `Value | Notes
---|---\n`;
                Object.keys(vivaldi[api][method]).forEach(enumerated => {
                    vapi += `\`${enumerated}\`|\n`;
                });
            } else if (method === 'exit'){
                vapi += `### vivaldi.${api}.${method}()\n`;
                vapi += 'Quits Vivaldi\n';
            } else if (method === 'showPasswordDialog'){
                vapi += `### vivaldi.${api}.${method}()\n`;
                vapi += 'Invokes OS Password Authenticator\n';
            } else {
                vapi += `### vivaldi.${api}.${method}()\n`;
                try {
                    vivaldi[api][method]();
                    vapi += 'Unknown arguments\n';
                } catch (e) {
                    let signature = e.message.replace('Error in invocation of ', '');
                    signature = signature.replace(': No matching signature.', '');
                    signature = signature.replace(`${api}.${method}(`, '');
                    signature = signature.replace(')', '');
                    let methodArgs = signature.split(',');
                    methodArgs = methodArgs.map(x => x.trim());
                    methodArgs = methodArgs.map(x => x.split(' '));
                    vapi += `Type | Argument | Notes
---|---|---\n`;
                    methodArgs.forEach(typeAndName => {
                        if(typeAndName[0]==='optional'){
                            vapi += `\`${typeAndName[1]}\`|${typeAndName[2]}|*(Optional)*\n`;
                        } else {
                            vapi += `\`${typeAndName[0]}\`|${typeAndName[1]}|\n`;
                        }
                    });
                }
            }
            vapi += '\n\n';
        });
    });
    console.log(vapi);
}

generateVivaldiAPI();
