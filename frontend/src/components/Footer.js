import { Container, Row, Col } from 'react-bootstrap'

import React from 'react'

function Footer() {
  return (
    <footer>
      <Container>
        <Row>
          <Col className='text-center'>Copyright &copy; ProShop</Col>
        </Row>
      </Container>
    </footer>
  )
}

export default Footer
