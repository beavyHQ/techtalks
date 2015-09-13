import React from "react";
import { Link } from "react-router";
import ReactLogo from "elements/ReactLogo";
import { Modal } from "./Modal";
import styles from './MainMenu.scss';
import classnames from 'classnames';

let MainMenuItems = []
let NavigationTools = []

export var registerMainMenuItem = i => MainMenuItems.push(i);
export var registerNavigationToolsItem = i => NavigationTools.push(i);

export class MainMenu extends React.Component {
	constructor(props) {
    super(props);
    this.state = {loginOpen: false};
  }

	render() {
		let logo = this.props.logo || 'https://raw.githubusercontent.com/thoughtbot/refills/master/source/images/placeholder_logo_1.png',
				loginModal = this.state.loginOpen ? <Modal isOpen={true} title="Login"><iframe src="/login?next=/refresh_session"></iframe></Modal> : null;
		return <div className={styles.navigation} role="banner">
						{loginModal}
					  <div className={styles.navigationWrapper}>
					    <Link to="app" className={styles.logo}>
					      <img src={logo} alt="Logo Image" />
					    </Link>
					    <a href="" className={styles.navigationMenuButton} id="js-mobile-menu">MENU</a>
					    <nav role="navigation">
					      <ul id="js-navigation-menu" className={classnames(styles.navigationMenu, styles.show)}>
					      	{MainMenuItems.map(x=>x.apply(this))}
					      </ul>
					    </nav>
					    <button onClick={this.toggleLogin.bind(this)}>Login</button>
					    <div className={styles.navigationTools}>
					    	{NavigationTools.map(x=>x.apply(this))}
					    </div>
					  </div>
				</div>;
	}
	toggleLogin(){
		console.log(this.state.loginOpen);
		this.setState({loginOpen: !this.state.loginOpen});
	}
}