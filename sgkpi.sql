-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 02-Abr-2025 às 03:06
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sgkpi`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_user'),
(2, 'Can change user', 1, 'change_user'),
(3, 'Can delete user', 1, 'delete_user'),
(4, 'Can view user', 1, 'view_user'),
(5, 'Can add objetivo_estrategico', 2, 'add_objetivo_estrategico'),
(6, 'Can change objetivo_estrategico', 2, 'change_objetivo_estrategico'),
(7, 'Can delete objetivo_estrategico', 2, 'delete_objetivo_estrategico'),
(8, 'Can view objetivo_estrategico', 2, 'view_objetivo_estrategico'),
(9, 'Can add rastreabilidade', 3, 'add_rastreabilidade'),
(10, 'Can change rastreabilidade', 3, 'change_rastreabilidade'),
(11, 'Can delete rastreabilidade', 3, 'delete_rastreabilidade'),
(12, 'Can view rastreabilidade', 3, 'view_rastreabilidade'),
(13, 'Can add meta', 4, 'add_meta'),
(14, 'Can change meta', 4, 'change_meta'),
(15, 'Can delete meta', 4, 'delete_meta'),
(16, 'Can view meta', 4, 'view_meta'),
(17, 'Can add log entry', 5, 'add_logentry'),
(18, 'Can change log entry', 5, 'change_logentry'),
(19, 'Can delete log entry', 5, 'delete_logentry'),
(20, 'Can view log entry', 5, 'view_logentry'),
(21, 'Can add permission', 6, 'add_permission'),
(22, 'Can change permission', 6, 'change_permission'),
(23, 'Can delete permission', 6, 'delete_permission'),
(24, 'Can view permission', 6, 'view_permission'),
(25, 'Can add group', 7, 'add_group'),
(26, 'Can change group', 7, 'change_group'),
(27, 'Can delete group', 7, 'delete_group'),
(28, 'Can view group', 7, 'view_group'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add content type', 9, 'add_contenttype'),
(34, 'Can change content type', 9, 'change_contenttype'),
(35, 'Can delete content type', 9, 'delete_contenttype'),
(36, 'Can view content type', 9, 'view_contenttype'),
(37, 'Can add session', 10, 'add_session'),
(38, 'Can change session', 10, 'change_session'),
(39, 'Can delete session', 10, 'delete_session'),
(40, 'Can view session', 10, 'view_session'),
(41, 'Can add kpi', 11, 'add_kpi'),
(42, 'Can change kpi', 11, 'change_kpi'),
(43, 'Can delete kpi', 11, 'delete_kpi'),
(44, 'Can view kpi', 11, 'view_kpi'),
(45, 'Can add objetivo_anual', 12, 'add_objetivo_anual'),
(46, 'Can change objetivo_anual', 12, 'change_objetivo_anual'),
(47, 'Can delete objetivo_anual', 12, 'delete_objetivo_anual'),
(48, 'Can view objetivo_anual', 12, 'view_objetivo_anual'),
(49, 'Can add atividade_anual', 13, 'add_atividade_anual'),
(50, 'Can change atividade_anual', 13, 'change_atividade_anual'),
(51, 'Can delete atividade_anual', 13, 'delete_atividade_anual'),
(52, 'Can view atividade_anual', 13, 'view_atividade_anual'),
(53, 'Can add acao', 14, 'add_acao'),
(54, 'Can change acao', 14, 'change_acao'),
(55, 'Can delete acao', 14, 'delete_acao'),
(56, 'Can view acao', 14, 'view_acao'),
(57, 'Can add processo', 15, 'add_processo'),
(58, 'Can change processo', 15, 'change_processo'),
(59, 'Can delete processo', 15, 'delete_processo'),
(60, 'Can view processo', 15, 'view_processo');

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(5, 'admin', 'logentry'),
(7, 'auth', 'group'),
(6, 'auth', 'permission'),
(8, 'auth', 'user'),
(9, 'contenttypes', 'contenttype'),
(1, 'login', 'user'),
(14, 'master', 'acao'),
(13, 'master', 'atividade_anual'),
(11, 'master', 'kpi'),
(4, 'master', 'meta'),
(12, 'master', 'objetivo_anual'),
(2, 'master', 'objetivo_estrategico'),
(15, 'master', 'processo'),
(3, 'master', 'rastreabilidade'),
(10, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-03-25 13:53:36.933386'),
(2, 'auth', '0001_initial', '2025-03-25 13:53:37.630853'),
(3, 'admin', '0001_initial', '2025-03-25 13:53:37.774487'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-03-25 13:53:37.791715'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-25 13:53:37.827896'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-03-25 13:53:37.905005'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-03-25 13:53:38.022937'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-03-25 13:53:38.046360'),
(9, 'auth', '0004_alter_user_username_opts', '2025-03-25 13:53:38.061384'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-03-25 13:53:38.122500'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-03-25 13:53:38.129762'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-03-25 13:53:38.146077'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-03-25 13:53:38.168955'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-03-25 13:53:38.190993'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-03-25 13:53:38.214990'),
(16, 'auth', '0011_update_proxy_permissions', '2025-03-25 13:53:38.227991'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-03-25 13:53:38.247992'),
(18, 'sessions', '0001_initial', '2025-03-25 13:53:38.305038'),
(19, 'login', '0001_initial', '2025-03-25 14:33:54.288721'),
(20, 'master', '0001_initial', '2025-03-26 00:44:56.662997'),
(21, 'master', '0002_rastreabilidade', '2025-03-27 13:42:17.215026'),
(22, 'master', '0003_meta', '2025-03-27 20:59:50.398640'),
(23, 'master', '0004_rastreabilidade_id_meta', '2025-03-27 22:57:28.869881'),
(24, 'master', '0002_rename_id_meta_rastreabilidade_id_tabela_meta', '2025-03-27 22:58:55.849771'),
(25, 'master', '0005_merge_20250327_2149', '2025-03-27 22:58:55.857768'),
(26, 'master', '0006_kpi', '2025-03-28 01:56:35.196092'),
(27, 'master', '0007_objetivo_anual', '2025-03-28 13:14:33.177869'),
(28, 'master', '0008_meta_id_kpi', '2025-03-29 01:02:41.079206'),
(29, 'master', '0009_atividade_anual', '2025-03-29 01:58:46.908834'),
(30, 'master', '0010_acao', '2025-03-29 20:39:34.127147'),
(31, 'master', '0011_processo', '2025-03-29 21:05:28.227457');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `login_user`
--

CREATE TABLE `login_user` (
  `id` int(11) NOT NULL,
  `username` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `perfil` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_acao`
--

CREATE TABLE `master_acao` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `data_registo` varchar(10) NOT NULL,
  `id_atividade_anual` int(11) NOT NULL,
  `id_departamento_responsavel` int(11) NOT NULL,
  `responsavel_nome` varchar(100) NOT NULL,
  `id_departamento_auxiliar` int(11) DEFAULT NULL,
  `responsavel_auxiliar_nome` varchar(100) NOT NULL,
  `id_processo` int(11) NOT NULL,
  `obs` varchar(500) DEFAULT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_acao`
--

INSERT INTO `master_acao` (`id`, `descricao`, `status`, `data_inicio`, `data_fim`, `data_registo`, `id_atividade_anual`, `id_departamento_responsavel`, `responsavel_nome`, `id_departamento_auxiliar`, `responsavel_auxiliar_nome`, `id_processo`, `obs`, `datecreate`, `dateupdate`) VALUES
(13, 'Acao 3', 1, '2025-03-30', '2025-03-31', '', 11, 3, 'Elton', 2, 'Aderito', 4, 'ok', '2025-03-31 00:10:14.186927', '2025-03-31 00:41:11.676974'),
(14, 'teste', 1, '2025-04-01', '2025-04-02', '31/03', 11, 2, 'Elton', 2, 'Aderito', 15, 'ok', '2025-04-01 20:36:32.898249', '2025-04-01 22:25:18.504029');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_atividade_anual`
--

CREATE TABLE `master_atividade_anual` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `id_objetivo_anual` int(11) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_atividade_anual`
--

INSERT INTO `master_atividade_anual` (`id`, `descricao`, `status`, `id_objetivo_anual`, `data_inicio`, `data_fim`, `datecreate`, `dateupdate`) VALUES
(11, 'Atividade Anual 1', 1, 14, '2025-03-01', '2025-03-31', '2025-03-30 20:47:56.900085', '2025-03-30 20:47:56.900085');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_departamento`
--

CREATE TABLE `master_departamento` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `datecreate` timestamp NOT NULL DEFAULT current_timestamp(),
  `dateupdate` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_departamento`
--

INSERT INTO `master_departamento` (`id`, `descricao`, `status`, `datecreate`, `dateupdate`) VALUES
(1, 'ABB', 1, '2025-03-30 23:27:49', '2025-03-30 23:27:49'),
(2, 'AGI', 1, '2025-03-30 23:27:49', '2025-03-30 23:27:49'),
(3, 'AIB', 1, '2025-03-30 23:27:49', '2025-03-30 23:27:49'),
(4, 'ARA', 1, '2025-03-30 23:27:49', '2025-03-30 23:27:49');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_kpi`
--

CREATE TABLE `master_kpi` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `id_objeto_estrategico` int(11) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_kpi`
--

INSERT INTO `master_kpi` (`id`, `descricao`, `status`, `id_objeto_estrategico`, `datecreate`, `dateupdate`) VALUES
(13, 'KPI 1', 1, 36, '2025-03-30 20:42:12.480708', '2025-03-30 20:42:33.832389');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_meta`
--

CREATE TABLE `master_meta` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL,
  `id_kpi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_meta`
--

INSERT INTO `master_meta` (`id`, `descricao`, `status`, `datecreate`, `dateupdate`, `id_kpi`) VALUES
(19, 'Meta 1', 1, '2025-03-30 20:42:55.247313', '2025-03-30 20:42:55.247313', 13);

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_objetivo_anual`
--

CREATE TABLE `master_objetivo_anual` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `id_kpi` int(11) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_objetivo_anual`
--

INSERT INTO `master_objetivo_anual` (`id`, `descricao`, `status`, `id_kpi`, `datecreate`, `dateupdate`) VALUES
(14, 'objetivo anual 1', 1, 13, '2025-03-30 20:45:10.876690', '2025-03-30 20:45:10.877693');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_objetivo_estrategico`
--

CREATE TABLE `master_objetivo_estrategico` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_objetivo_estrategico`
--

INSERT INTO `master_objetivo_estrategico` (`id`, `descricao`, `status`, `datecreate`, `dateupdate`) VALUES
(36, 'Objetivo 1', 1, '2025-03-30 20:41:37.344339', '2025-03-30 20:41:37.344339');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_processo`
--

CREATE TABLE `master_processo` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `datecreate` datetime(6) NOT NULL,
  `dateupdate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_processo`
--

INSERT INTO `master_processo` (`id`, `descricao`, `status`, `datecreate`, `dateupdate`) VALUES
(1, 'Constituição de instituições financeiras com sede em CV', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(2, 'Estabelecimento de sucursais de instituições financeiras com sede no estrangeiro', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(3, 'Alteração da denominação', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(4, 'Alteração do objeto', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(5, 'Alteração do tipo de instituição', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(6, 'Alteração do local da sede', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(7, 'Alteração do capital social', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(8, 'Alteração das categorias de ações', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(9, 'Alteração da estrutura da administração ou da fiscalização', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(10, 'Alteração da limitação dos poderes dos órgãos de administração ou de fiscalização', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(11, 'Alteração das disposições relativas à dissolução', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(12, 'Exercício de funções do órgão de administração ou fiscalização', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(13, 'Exercício de funções de titulares de funções chave', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(14, 'Fusão de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(15, 'Cisão de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(16, 'Acumulação de cargos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(17, 'Aquisição/aumento de participação qualificada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(18, 'Alienação/diminuição de participação qualificada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(19, 'Inscrição de agentes de prestadores de serviços de pagamentos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(20, 'Estabelecimento no estrangeiro de sucursais, filiais ou escritórios de representação de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(21, 'Dissolução voluntária', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(22, 'Registo de constituição de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(23, 'Registo de início de atividade de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(24, 'Registos de estabelecimento de sucursais e escritórios de representação de instituições financeiras ', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(25, 'Registo de alterações estatutárias', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(26, 'Registos de acordos parassociais', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(27, 'Registo de delegação de poderes de gestão', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(28, 'Registo de outros elementos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(29, 'Registos de alterações de elementos sucursais e escritórios de representação de instituições finance', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(30, 'Registo de membros de órgãos sociais', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(31, 'Registo de titulares de funções chaves', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(32, 'Registo agências/balcões', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(33, 'Registo de sucursais, filiais e escritórios de representação no estrangeiro', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(34, 'Registo de agentes prestadores de serviços de pagamentos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(35, 'Registo de acionistas titulares de participação qualificada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(36, 'Registo da dissolução voluntária', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(37, 'Comunicações de instituições', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(38, 'Comunicações de sucursais e escritórios de representação de instituições financeiras com sede no est', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(39, 'Alteração de dados de membros de órgãos sociais', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(40, 'Alteração de dados de titulares de funções chave', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(41, 'Alterações de participantes qualificados', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(42, 'Alterações de sucursais e escritórios de representação no estrangeiro de instituições financeiras co', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(43, 'Validação técnica e funcional dos reportes financeiros e prudenciais recebidos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(44, 'Monitorização de indicadores de solidez financeira setor bancário', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(45, 'Monitorização de indicadores de solidez financeira de outras IFs', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(46, 'Avaliação de indicadores de solidez financeira do setor bancário', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(47, 'Avaliação de indicadores de solidez financeira de outras IFs', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(48, 'Monitorização de indicadores essenciais  da instituição supervisionada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(49, 'Análise do modelo de negócio da instituição supervisionada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(50, 'Análise do governo interno e dos controlos a nível da instituição', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(51, 'Análise dos riscos para os fundos próprios', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(52, 'Análise dos riscos para a liquidez e para o financiamento', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(53, 'Análise da adequação dos fundos próprios da instituição', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(54, 'Análise da adequação dos recursos de liquidez da instituição', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(55, 'Análise do perfil de risco da instituição e a sua viabilidade', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(56, 'Análise anual da evolução da instituição e perspetivas', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(57, 'Pedidos de informação/esclarecimentos', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(58, 'Análises temáticas', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(59, 'Inspeção da instituição supervisionada', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(60, 'Cessação de autorizações concedidas', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(61, 'Cessação de autorizações de sucursais e escritórios de representação de instituições financeiras com', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(62, 'Acompanhamento do processo de dissolução e liquidação da instituição', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000'),
(63, 'Monitorização do exercício ilegal de atividades', 1, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------

--
-- Estrutura da tabela `master_rastreabilidade`
--

CREATE TABLE `master_rastreabilidade` (
  `id` int(11) NOT NULL,
  `descricao` varchar(200) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `datecreate` datetime NOT NULL,
  `dateupdate` datetime NOT NULL,
  `id_tabela_meta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `master_rastreabilidade`
--

INSERT INTO `master_rastreabilidade` (`id`, `descricao`, `status`, `datecreate`, `dateupdate`, `id_tabela_meta`) VALUES
(20, 'Rastreabilidade', 1, '2025-03-30 20:43:27', '2025-03-30 20:43:27', 19);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Índices para tabela `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Índices para tabela `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Índices para tabela `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Índices para tabela `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Índices para tabela `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Índices para tabela `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Índices para tabela `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Índices para tabela `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Índices para tabela `login_user`
--
ALTER TABLE `login_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Índices para tabela `master_acao`
--
ALTER TABLE `master_acao`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_atividade_anual`
--
ALTER TABLE `master_atividade_anual`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_departamento`
--
ALTER TABLE `master_departamento`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_kpi`
--
ALTER TABLE `master_kpi`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_meta`
--
ALTER TABLE `master_meta`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_objetivo_anual`
--
ALTER TABLE `master_objetivo_anual`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_objetivo_estrategico`
--
ALTER TABLE `master_objetivo_estrategico`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_processo`
--
ALTER TABLE `master_processo`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `master_rastreabilidade`
--
ALTER TABLE `master_rastreabilidade`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de tabela `login_user`
--
ALTER TABLE `login_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `master_acao`
--
ALTER TABLE `master_acao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `master_atividade_anual`
--
ALTER TABLE `master_atividade_anual`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `master_departamento`
--
ALTER TABLE `master_departamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `master_kpi`
--
ALTER TABLE `master_kpi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `master_meta`
--
ALTER TABLE `master_meta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `master_objetivo_anual`
--
ALTER TABLE `master_objetivo_anual`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `master_objetivo_estrategico`
--
ALTER TABLE `master_objetivo_estrategico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de tabela `master_processo`
--
ALTER TABLE `master_processo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT de tabela `master_rastreabilidade`
--
ALTER TABLE `master_rastreabilidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Limitadores para a tabela `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Limitadores para a tabela `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limitadores para a tabela `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Limitadores para a tabela `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
