describe('Landing Page', () => {
    it('Should be able to submit from with email', () => {
        cy.visit('http://127.0.0.1:8000/')
        // cy.get('h1').contains('Hit Me!')
        cy.get('input[name="email"]').type('pepea.23@live.com')
        cy.get('button[type="submit"]').click()

        const admin = cy
        admin.visit('http://127.0.0.1:8000/admin')
        admin.get('input[name="username"')
        .type('pekpeaping').get('input[name="password"]')
        .type('p').get('input[type="submit"]').click()
        admin.get('.model-hitter > th > a').click()
        admin.get('.field-email > a').should('contain','pepea.23@live.com')
    })
})
