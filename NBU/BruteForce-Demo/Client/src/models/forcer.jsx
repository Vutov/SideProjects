function generatePasswords() {
    let passwords = [];
    for (let i = 0; i < 10000; i++) {
        let password = ('000' + i).slice(-4);
        passwords.push(password);
    }

    return passwords;
}

export { generatePasswords }