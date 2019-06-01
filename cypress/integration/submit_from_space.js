describe('Landing Page', () => {
    it('Should be able to submit from with email', () => {
        cy.visit('http//localhost:8000')
        cy.get('h1').contains('Hit Me!')
        cy.get('input[name="email"]').type('pepea.23@live.com')
        cy.get('button[type="submit"]').click()

        const admin = cy
        admin.visit('http//localhost:8000/admin')
        admin.get('input[name="username"')
        .type('pepea').get('input[name="password"]')
        .type('Pronto123').get('button[type]="submit"').click()
        admin.get('xyz').click().get('abc').click().contains('pepea.23@live.com')

    })
})
